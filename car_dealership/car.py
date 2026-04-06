class Car:
    def __init__(self, make, model, year, price, mileage, id=None):

        if year <= 0:
            raise ValueError("Year must be a positive integer.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if mileage < 0:
            raise ValueError("Mileage cannot be negative.")
        
        self.id = id
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.mileage = mileage

    def __str__(self):

        id_display = f"ID: {self.id}" if self.id else "NEW"

        return (
            f"[{id_display}] {self.year} {self.make} {self.model} | "
            f"${self.price:,.2f} | {self.mileage:,} km"
        )
    
    def to_tuple (self):
        return (self.make, self.model, self.year, self.price, self.mileage)
