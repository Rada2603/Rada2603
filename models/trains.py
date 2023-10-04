from models.train import Train


class Trains:
    def __init__(self, path_to_file):
        self.list_of_train = []
        self.path_to_file = path_to_file

    def add_train(self, train: Train):
        self.list_of_train.append(train)

    def list_train(self):
        for train in self.list_of_train:
            print(train)

    def initialise_train(self):
        t = open(self.path_to_file, "r")
        for train in t:
            train = Train(
                train.split()[0], train.split()[1], train.split()[2], train.split()[3]
            )
            self.add_train(train)

    def find_transport(self, meal_t, starting_address_t, final_address_t) -> Train:
        for train in self.list_of_train:
            if (
                train.meal == meal_t
                and train.starting_address == starting_address_t
                and train.final_address == final_address_t
            ):
                return Train(
                    train.meal, train.starting_address, train.final_address, train.clases
                )
