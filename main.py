from utils import check_option
from models.agents import Agents
from models.clients import Clients
from utils import check_option_a
from utils import check_option_c
from models.hotels import Hotels
from models.apartments import Apartments
from models.arrgaments import Arrgaments
from models.a_plane import A_planes
from models.train import Trains
from models.creating_an_arrangement import Creating_an_arrngamment


def main():
    print("\nWelcome to agency")
    agents = Agents(r"data\agents.txt")
    agents.initialise_agent()
    clients = Clients(r"data\clients.txt")
    clients.initialise_client()
    hotels = Hotels(r"data\hotel.txt")
    hotels.initialise_hotel()
    apartment = Apartments(r"data\apartment.txt")
    apartment.initialise_apartment()
    arrgaments = Arrgaments(r"data\arrangement.txt")
    arrgaments.initialise_arrgement()
    a_planes = A_planes(r"data\a_plane.txt")
    a_planes.initialise_plane()
    trains = Trains(r"data\train.txt")
    trains.initialise_train()
    arrgament_1 = Creating_an_arrngamment()
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
            age = agents.check_agent(names, passwords)
            if not age:
                continue
            while True:
                print("Select option")
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
                if option_a == "2":
                    print("select accommodation")
                    print("1.hotel")
                    print("2.apartment")
                    option_h = input("select an option")
                    print(f"option_h:{option_h}")
                    if option_h == "1":
                        hotels.list_hotel()
                        print("select the hotel")
                        surface_1 = input("surface")
                        hotel_1 = hotels.find_hotels(surface_1)
                        arrgament_1.add_arrngamment(hotel_1)
                        if not hotel_1:
                            continue
                    if option_h == "2":
                        apartment.list_apartment()
                        print("select the apartment")
                        surface_2 = input("surface_a")
                        apartment_2 = apartment.find_apartment(surface_2)
                        arrgament_1.add_arrngamment(apartment_2)
                        if not apartment_2:
                            continue

        if option == "b":
            name_c = input("name")
            password_c = input("password")
            cli = clients.check_client(name_c, password_c)
            if not cli:
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

