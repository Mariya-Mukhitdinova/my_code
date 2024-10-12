class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        return self.brand, self.model, self.year

class Car(Vehicle):
    def __init__(self, brand, model, year, hybrid):
        super().__init__(brand, model, year)
        self.hybrid = hybrid
    def display_info(self):
        return self.brand, self.model, self.year, self.hybrid

class Motorcycle(Vehicle):
    def __init__(self,  brand, model, year, electricity):
        super().__init__(brand, model, year)
        self.electricity = electricity

    def display_info(self):
        return self.brand, self.model, self.year, self.electricity