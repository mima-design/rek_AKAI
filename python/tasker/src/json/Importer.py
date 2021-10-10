import json


class Importer:

    def __init__(self):
        pass

    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        self.file = open("taski.json")
        self.decoded_file = json.load(self.file)

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        return self.decoded_file
