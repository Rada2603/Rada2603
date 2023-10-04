from models.transport import Transport_device


class Train(Transport_device):
    def __init__(self, meal, starting_address, final_address, clases):
        super().__init__(meal, starting_address, final_address, clases)

    def __str__(self) -> str:
        return f"{self.meal}-{self.starting_address}-{self.final_address}-{self.clases}"
