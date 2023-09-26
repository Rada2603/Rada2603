from models.accommodation import Accommodation
from models.transport import Transport_device


class Creating_an_arrngamment:
    def __init__(self):
        self.list_of_arrngamment = []
        self.list_of_transport = []

    def add_arrngamment(self, arrnga: Accommodation):
        self.list_of_arrngamment.append(arrnga)

    def list_arrngament(self):
        for arrnga in self.list_of_arrngamment:
            print(arrnga)

    def add_transport(self, trans: Transport_device):
        self.list_of_transport.append(trans)

    def list_transport(self):
        for trans in self.list_of_transport:
            print(trans)
