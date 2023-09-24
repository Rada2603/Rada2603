class User:
    def __init__(self, Ime, Prezime, name, password, many):
        self.name = name
        self.password = password
        self.Ime = Ime
        self.Prezime = Prezime
        

    def __str__(self) -> str:
        return f"{self.Ime}-{self.Prezime}-{self.name}-{self.password}"