from models.creating_an_arrangement import Creating_an_arrngamment
from models.creating_an_arrangement import Createarggament

class Packages:
    def __init__(self):
        self.list_package = []

    def add_packages(self, packages: Createarggament):
        self.list_package.append(packages)

    def list_packages(self):
        for package in self.list_package:
            print(package)
    
    def find_package(self, nomber_k) -> Createarggament:
        for package in self.list_package:
            if int(package.nomber) == int(nomber_k):
                package.nomber == str(int(package.nomber))
                print("1111111")
                return Createarggament(package.nomber, package.acommodate, package.transport)
                
                