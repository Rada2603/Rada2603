from models.accommodation import Accommodation


class Hotels:
    def __init__(self, path_to_file) -> None:
        self.list_of_hotel = []
        self.path_to_file = path_to_file

    def add_hotel(self, hotel: Accommodation):
        self.list_of_hotel.append(hotel)

    def list_hotel(self):
        for hotel in self.list_of_hotel:
            print(hotel)

    def initialise_hotel(self):
        f = open(self.path_to_file, "r")
        for h in f:
            hotel = Accommodation(h.split('-')[0], h.split('-')[1], h.split('-')[2], h.split('-')[3], h.split('-')[4])
            self.add_hotel(hotel)
            