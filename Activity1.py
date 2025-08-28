# Activity 1: My own class (CeraVe Skincare Example)

class CeraVeProduct:
    def __init__(self, name, product_type, price):
        self.name = name                 # e.g. "CeraVe Hydrating Cleanser"
        self.product_type = product_type # e.g. "Cleanser", "Moisturizer"
        self.price = price               # e.g. 12.99
        print(f"CeraVe product '{self.name}' has been created!")

     # Method 1: Show product details
    def show_details(self):
            print(f"Product:{self.name}")
            print(f"Type: {self.product_type}")
            print(f"Price: KSH{self.price}")

    # Method 2: Apply a discount
    def apply_discount(self, percent):
            discount_amount = (percent/100) * self.price
            self.price -= discount_amount
            print(f"Discount of {percent}% applied! New price: KSH{self.price}")

# --- Testing the class ---

# Create objects
cleanser = CeraVeProduct("CeraVe Hydrating Cleanser", "Cleanser", 1500)
moisturizer = CeraVeProduct("CeraVe Moisturizing Cream", "Moisturizer", 2500)

# Show details
cleanser.show_details()
moisturizer.show_details()

# Apply discount
moisturizer.apply_discount(10)   # apply 10% discount
moisturizer.show_details()

# Subclass that inherits from CeraVeProduct
class Moisturizer(CeraVeProduct):
    def __init__(self, name, price, spf, skin_type):
        # Call the parent constructor (CeraVeProduct)
        super().__init__(name, "Moisturizer", price)
        self.spf = spf
        self.skin_type = skin_type

    # Overriding show_details to include extra info
    def show_details(self):
        super().show_details()
        print(f"SPF: {self.spf}")
        print(f"Skin Type: {self.skin_type}")

# Create moisturizer object from subclass
moisturizer_spf = Moisturizer("CeraVe AM Facial Moisturizing Lotion", 2000, 30, "Normal to Dry")
moisturizer_spf.show_details()
