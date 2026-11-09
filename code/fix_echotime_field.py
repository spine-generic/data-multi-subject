import json
from pathlib import Path

class FixEchoField:
    def __init__(self):
        pass

    def update_bids_sidecar(self, sidecar_file):
        """
        Update the sidecar by correcting the EchoTime field if it is wrongly written
        """

        json_path = Path(sidecar_file)

        if json_path.exists(): # sidecar file loading
            with open(json_path, 'r', encoding='utf-8') as f:
                sidecar = json.load(f)
        else:
            sidecar = {}

        echo_time = sidecar.get("EchoTime")

        if echo_time is None:
            return

        if self.assess_field_format(echo_time): # if the format is correct, do not touch
            return

        if isinstance(echo_time, str):
            echo_time = self.string_to_list(echo_time)

        sidecar["EchoTime"] = echo_time

        if not self.assess_field_format(sidecar["EchoTime"]):
            raise TypeError("EchoTime field has not the good type (list or number) and cannot be converted correctly (is not a string)")

        with open(json_path, 'w', encoding='utf-8') as f: # saving of the updated sidecar
            json.dump(sidecar, f, indent=4, ensure_ascii=False)

    def assess_field_format(self, echo_time) -> bool:
        """
        Given a string, returns true if it has the correct format according to BIDS convention (list or number) and false else
        """
        if isinstance(echo_time, (int, float)):
            return True
        if isinstance(echo_time, list):
            return all(isinstance(x, (int, float)) for x in echo_time)
        return False

    def string_to_list(self, echo_time):
        """
        Convert the string into the correct format
        """
        elements = [float(x.strip()) for x in echo_time.split(",") if x.strip()]
        if len(elements) == 1:
            return elements[0]
        return elements

    def crawl_dataset(self):
        """
        Process the whole dataset to fix incorrectly written EchoTime fields
        """
        dataset_path = Path(__file__).resolve().parent.parent
        sidecars = self.find_all_sidecars(dataset_path)

        for sidecar in sidecars:
            self.update_bids_sidecar(sidecar)

        return

    def find_all_sidecars(self, bids_dir, exclude_derivatives=True):
        """
        Parcourt le dataset BIDS et retourne la liste de tous les fichiers JSON sidecars.
        """

        bids_path = Path(bids_dir)
        sidecars = []

        for json_path in bids_path.glob("sub-*/**/*.json"):
            if exclude_derivatives and "derivatives" in json_path.parts:
                continue
            sidecars.append(json_path)
        return sidecars


if __name__=="__main__":
    fix_dataset = FixEchoField()
    fix_dataset.crawl_dataset()