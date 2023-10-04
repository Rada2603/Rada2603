from models.accommodation import Accommodation


class Apartment(Accommodation):
    def __init__(self, surface, beds, type, adress):
        super().__init__(surface, beds, type, adress)

    def __str__(self) -> str:
        return f"{self.surface}-{self.beds}-{self.type}-{self.adress}"
