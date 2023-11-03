class Arrangement:
    def __init__(self, insurance, type, departure, returns):
        self.insurance = insurance
        self.type = type
        self.departure = departure
        self.returns = returns

    def __str__(self) -> str:
        return f"{self.insurance}-{self.type}-{self.departure}-{self.returns}"
    

class Arrgaments:
    def __init__(self, path_to_file):
        self.list_of_arrgament = []
        self.path_to_file = path_to_file

    def add_arrgement(self, arrgement: Arrangement):
        self.list_of_arrgament.append(arrgement)

    def list_arrgement(self):
        for arrgament in self.list_of_arrgament:
            print(arrgament)

    def initialise_arrgement(self):
        f = open(self.path_to_file, "r")
        for s in f:
            arrgament = Arrangement(s.split("-")[0], s.split("-")[1], s.split("-")[2], s.split("-")[3] )
            self.add_arrgement(arrgament)





        
        