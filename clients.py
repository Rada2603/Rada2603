from models.user import User


class Clients:
    def __init__(self, path_to_file) -> None:
        self.list_of_client = []
        self.path_to_file = path_to_file

    def add_client(self, client: User):
        self.list_of_client.append(client)

    def list_client(self):
        for client in self.list_of_agent:
            print(client)
    

    def initialise_users(self):
        f = open(self.path_to_file, "r")
        for a in f:
            client = User(a.split()[0], a.split()[1], a.split()[2], a.split()[3], a.split()[4])
            self.add_client(client)
        
    def check_client(self, Name: str, Password: str) -> User:
        for user in self.list_of_client:
            if user.name == Name and user.password == Password:
                print("ok")
                return True
               
        else:
            print("wrong")