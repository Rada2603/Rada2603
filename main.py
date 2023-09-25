from utils import check_option
from models.agents import Agents
from models.clients import Clients
from utils import check_option_a
from utils import check_option_c
from models.hotel import Hotels


def main():
    print("\nWelcome to agency")
    agents = Agents(r"data\agents.txt")
    agents.initialise_users()
    clients = Clients(r"data\clients.txt")
    clients.initialise_users()
    agents.list_agent()
    clients.list_client()
    hotels = Hotels(r"data\hotel.txt")
    hotels.initialise_hotel()
    hotels.list_hotel()
    while True:
        print("____please login___")
        print("a. I am agent")
        print("b. I am client")
        option = input("select an  option")
        print(f"option:{option}")
        if not check_option(option):
            continue
        if option == "a":
            names = input("name")
            passwords = input("password")
            agents.check_agent(names, passwords)
            if not agents.check_agent(names, passwords):
                continue
            while True:
                print("Select an option")
                print("1.Logout")
                print("2.creating an arrangement")
                print("3.Creating a package")
                print("4.Deleting an arrangement")
                option_a = input("Select an option")
                print(f"option_a:{option_a}")
                if not check_option_a(option_a):
                    break  
                if option_a == "1":
                    print("___Exit___")
                    break
                #if option_a == "2":

        if option == "b":
            name_c = input("name")
            password_c = input("password")
            clients.check_client(name_c, password_c)
            if not clients.check_client(name_c, password_c):
                continue
            while True:
                print("Select an option")
                print("1.Logout")
                print("2.Creating a package")
                print("3.Package rental")
                print("4.Package cancellation")
                print("5.Payment")
                option_c = input("Select an option")
                print(f"option_a:{option_c}")
                if not check_option_c(option_c):
                    break  
                if option_c == "1":
                    print("___Exit___")
                    break


if __name__ == "__main__":
    main()

