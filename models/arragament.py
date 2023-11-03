class Arragament:
    def __init__(self, insurance, travel, departure, returns, transportation):
        self.insurance = insurance
        self.travel = travel
        self.departure = departure
        self.returns = returns
        self.transportation = transportation

    def __str__(self) -> str:
        return f"{self.insurance}-{self.travel}-{self.departure}-{self.returns}-{self.transportation}"
    