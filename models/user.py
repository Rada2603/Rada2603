class User:
    def __init__(self, names, surname, name, password, many):
        self.names = names
        self.surname = surname
        self.name = name
        self.password = password
        self.many = many

    def __str__(self) -> str:
        return f"{self.names}-{self.surname}-{self.name}-{self.password}-{self.many}"