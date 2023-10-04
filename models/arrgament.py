class Arrgament:
    def __init__(self, insurance, type, departure, returns):
        self.insurance = insurance
        self.type = type
        self.departure = departure
        self.returns = returns
        
    def __str__(self) -> str:
        return f"{self.insurance}-{self.type}-{self.departure}-{self.returns}"
