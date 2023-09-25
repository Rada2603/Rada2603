class Accommodation:
    def __init__(self, surface, beds, type, adress, stars):
        self.surface = surface
        self.beds = beds
        self.type = type
        self.adress = adress
        self.stars = stars

    def __str__(self) -> str:
        return f"{self.surface},{self.beds},{self.type},{self.adress},{self.stars}"