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
    
    
                
                