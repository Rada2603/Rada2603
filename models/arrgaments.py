from models.arragament import Arragament


class Argaments:
    def __init__(self) -> None:
        self.list_of_arga = []

    def add_arga(self, argaa: Arragament):
        self.list_of_arga.append(argaa)

    def list_arga(self):
        for argaa in self.list_of_arga:
            print(argaa)