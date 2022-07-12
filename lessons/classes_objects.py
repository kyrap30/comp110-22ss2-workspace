"""Example of a class and object instantiation."""

class Pizza:
    """Models the ideas of a Pizza."""
    
    # Attribute Definition
    size: str = 
    toppings: int
    extra_cheese: bool


#method
    def price(self, tax: float) -> float:
        """Calculate price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total +=10.0
        else:
            total += 8.0
        
        total += self * 0.75
        
        if self.extra_cheese:
            total += 1.0

        total *= tax

        return total 


a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")