class Customers:
    def __init__(self, name, bev, food, total):
        self.name = name
        self.bev = bev
        self.food = food
        self.total = total

    greeting = "Welcome to Coffee Palace!"


c_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customers("Elaine", "Strawberry frappuccino", "Tuna Wrap", 270)
c_3 = Customers("Samirah", "Ice coffee latte", "Cinnamon roll", 225)
c_4 = Customers("Jerry", "Caramel Macchiato", "Glazed doughnut", 230)
c_5 = Customers("Paz", "Ice tea", "Blueberry pancakes", 315)

print(Customers.greeting)
print(c_1.name, c_1.bev, c_1.food, c_1.total)
print(c_2.name, c_2.bev, c_2.food, c_2.total)
