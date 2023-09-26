from models.transport import Transport_device


class Train(Transport_device):
    def __init__(self, meal, starting_address, final_address):
        super().__init__(meal, starting_address, final_address)

    def __str__(self) -> str:
        return f"{self.meal}-{self.starting_address}-{self.final_address}"
    

class Trains:
    def __init__(self, path_to_file):
        self.list_of_train = []
        self.path_to_file = path_to_file

    def add_train(self, train: Transport_device):
        self.list_of_train.append(train)
    
    def list_train(self):
        for train in self.list_of_train:
            print(train)

    def initialise_train(self):
        t = open(self.path_to_file, "r")
        for train in t:
            train = Train(train.split()[0], train.split()[0], train.split()[0])
            self.add_train(train)
        