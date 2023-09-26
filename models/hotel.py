from models.accommodation import Accommodation


class Hotel(Accommodation):
    def __init__(self, surface, beds, type, adress, stars):
        super().__init__(surface, beds, type, adress)       
        self.stars = stars

    def __str__(self) -> str:
        return f"{self.surface}-{self.beds}-{self.type}-{self.adress}-{self.stars}" 



