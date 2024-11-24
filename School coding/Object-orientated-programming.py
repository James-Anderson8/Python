import csv
class Good:
    discount_price = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to recieved arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0" 
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Execute actions
        Good.all.append(self)
    
    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount_price

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:\github\philanderson-co-uk\james\python\School coding\instances.csv', 'r') as f:
            reader = csv.DictReader(f)
            goods = list(reader)
        for good in goods:
            print(good)

    def __repr__(self):
        return f"{self.name}, ${self.price}, {self.quantity}"
    
#good1 = Good("Gloves", 20, 8)
#good2 = Good("Mouth guard", 10, 5)
#good3 = Good("Dumbbell", 30, 10)
#good4 = Good("Knuckle guard", 40, 3)
#good5 = Good("Head guard", 50, 2)

Good.instantiate_from_csv()



