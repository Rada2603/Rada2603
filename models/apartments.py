from models.apartment import Apartment


class Apartments:
    def __init__(self, path_to_file) -> None:
        self.list_of_apartment = []
        self.path_to_file = path_to_file

    def add_apartment(self, apartment: Apartment):
        self.list_of_apartment.append(apartment)

    def list_apartment(self):
        for apartment in self.list_of_apartment:
            print(apartment)

    def initialise_apartment(self):
        f = open(self.path_to_file, "r")
        for ap in f:
            apartment = Apartment(
                ap.split("-")[0], ap.split("-")[1], ap.split("-")[2], ap.split("-")[3]
            )
            self.add_apartment(apartment)

    def find_apartment(self, surface_2) -> Apartment:
        for apartment in self.list_of_apartment:
            if apartment.surface == surface_2:
                return Apartment(
                    apartment.surface, apartment.beds, apartment.type, apartment.adress
                )
        else:
            print("wrong")
