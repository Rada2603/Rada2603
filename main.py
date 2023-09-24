from utils import check_option
from models.agents import Agents
from models.clients import Clients
from utils import check_option_a


def main():
    print("\nWelcome to agency")
    Agent = Agents(r"data\agents.txt")
    Agent.initialise_users()
    Client = Clients(r"data\agents.txt")
    Client.initialise_users()
    while True:
        print("____please login___")
        print("a. I am agent")
        print("b. I am client")
        option = input("select an  option")
        print(f"option:{option}")
        if not check_option(option):
            continue
        if option == "a":
            Name = input("name")
            Password = input("password")
            Agent.check_agent(Name, Password)
            if not  Agent.check_agent(Name, Password):
                continue
            while True:
                print("Select an option")
                print("1.Logout")
                print("2.Creating  an engagement")
                print("3.Creating a package")
                print("4.Deleting an engagement")
                option_a = input("Select an option")
                print(f"option_a:{option_a}")
                print("===========")
                if not check_option_a(option_a):
                    print("pogresno")
                break
                   
        if option == "b":
            Name = input("name")
            Password = input("password")
            Client.check_client(Name, Password)


if __name__ == "__main__":
    main()
