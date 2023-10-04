from models.accommodation import Accommodation
from models.transport import Transport_device


class Createarggament:
    def __init__(self, nomber, acommodate, transport):
        self.nomber = nomber
        self.acommodate = acommodate
        self.transport = transport

    def __str__(self) -> str:
        return f"{self.nomber}.{self.acommodate},{self.transport}"
    

class Creating_an_arrngamment:
    def __init__(self):
        self.list_of_arrngamment = []

    def add_argament(self, arranga) -> Createarggament:
        self.list_of_arrngamment.append(arranga)
        print("222222")
        
    def list_argament(self):
        for arranga in self.list_of_arrngamment:
            print(arranga)
        
    def find_package(self, nomber_k) -> Createarggament:
        for package in self.list_of_arrngamment:
            if int(package.nomber) == int(nomber_k):
                package.nomber == str(int(package.nomber))
                print("1111111")
                return nomber_k
   
    
