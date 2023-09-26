from models.user import User


class Agent(User):
    def __init__(self, names, surname, name, password):
        super().__init__(names, surname, name, password)
        
    def __str__(self) -> str:
        return f"{self.names}-{self.surname}-{self.name}-{self.password}"   
    

class Agents:
    def __init__(self, path_to_file):
        self.list_of_agent = []
        self.path_to_file = path_to_file

    def add_agent(self, agent: User):
        self.list_of_agent.append(agent)

    def list_agent(self):
        for agent in self.list_of_agent:
            print(agent)

    def initialise_agent(self):
        f = open(self.path_to_file, "r")
        for a in f:
            agent = Agent(a.split()[0], a.split()[1], a.split()[2], a.split()[3])
            self.add_agent(agent)
        
    def check_agent(self, names: str, passwords: str) -> bool:
        for user in self.list_of_agent:
            if user.name == names and user.password == passwords:
                print("You have snged up")
                return True
        else:
            print(">>>>wrong\n")
            return False  
            
            