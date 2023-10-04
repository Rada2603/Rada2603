from utils import check_option
from models.agents import Agents
from models.clients import Clients
from utils import check_option_a
from utils import check_option_c
from models.hotels import Hotels
from models.apartments import Apartments
from models.arrgaments import Arrgaments
from models.a_plane import A_planes
from models.trains import Trains
from models.creating_an_arrangement import Creating_an_arrngamment
from models.creating_an_arrangement import Createarggament
from models.packages import Packages
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
    packages = Packages()
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
                        nomber_1 = input("nomber")
                        surface_1 = input("surface")
                        hotel_1 = hotels.find_hotels(surface_1)
                        
                        if not hotel_1:
                            continue
                    if option_h == "2":
                        apartment.list_apartment()
                        print("select the apartment")
                        nomber_1 = input("nomber")
                        surface_1 = input("surface_a")
                        hotel_1 = apartment.find_apartment(surface_1)
                        if not hotel_1:
                            continue
                    print("select transport")
                    print("1.train")
                    print("2.a_plane")
                    option_t = input("select an option")
                    print(f"option_t:{option_t}")
                    if option_t == "1":
                        trains.list_train()
                        meal_t = input("meal")
                        starting_address_t = input("starting_address")
                        final_address_t = input("final_addres")
                        transport_1 = trains.find_transport(meal_t, starting_address_t, final_address_t)
                        arrgaments_1 = Createarggament(nomber_1, hotel_1, transport_1)
                        arrgament_1.add_argament(arrgaments_1)
                        print(arrgaments_1)
                        print("--------")
                        if not transport_1:
                            continue
                    if option_t == "2":
                        a_planes.list_planes()
                        meal_t = input("meal")
                        starting_address_t = input("starting_address")
                        final_address_t = input("final_addres")
                        transport_1 = a_planes.find_planes(meal_t, starting_address_t, final_address_t)
                        arrgaments_1 = Createarggament(nomber_1, hotel_1, transport_1)
                        arrgament_1.add_argament(arrgaments_1)
                        print(arrgaments_1)
                        print("--------")
                if option_a == "3":
                    arrgament_1.list_argament() 
                    print("select option")
                    nomber = input("nomber is :")
                    nomber_k = arrgament_1.find_package(nomber)
                    print("000000")
                    packages_1 = Createarggament(nomber_k, hotel_1, transport_1)
                    print("55555555")
                    packages.add_packages(packages_1)
                    print("44444")
                    packages.list_packages()

                    
                    

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
