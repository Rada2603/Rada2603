class Createarggament:
    def __init__(self, nomber, acommodate, transport):
        self.nomber = nomber
        self.acommodate = acommodate
        self.transport = transport

    def __str__(self) -> str:
        return f"{self.nomber}.{self.acommodate},{self.transport}"