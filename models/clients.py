from models.user import User


class Client(User):
    def __init__(self, names, surname, name, password, money):
        super().__init__(names, surname, name, password)
        self.money = money

    def __str__(self) -> str:
        return f"{self.names}-{self.surname}-{self.name}-{self.password}-{self.money}"


class Clients:
    def __init__(self, path_to_file) -> None:
        self.list_of_client = []
        self.path_to_file = path_to_file

    def add_client(self, client: User):
        self.list_of_client.append(client)

    def list_client(self):
        for client in self.list_of_client:
            print(client)

    def initialise_client(self):
        f = open(self.path_to_file, "r")
        for a in f:
            client = Client(
                a.split()[0], a.split()[1], a.split()[2], a.split()[3], a.split()[4]
            )
            self.add_client(client)

    def check_client(self, name_c: str, password_c: str) -> User:
        for user in self.list_of_client:
            if user.name == name_c and user.password == password_c:
                print("You have snged up")
                return True
        else:
            print(">>>>wrong\n")
