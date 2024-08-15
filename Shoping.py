class Shop:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_cart(self, product_name, price, quantity):
        self.cart.append({"item": product_name, "price": price, "quantity": quantity})

    def checkout(self, payment):
        price = 0
        for item in self.cart:
            price += item["price"] * item["quantity"]
        if price > payment:
            print("Insufficient balance")
        elif price < payment:
            rev = payment - price
            print("Thanks for Shopping . Here is your Change", rev, "Taka")
        else:
            print("Thanks for Shopping . Come again sir ")


shoping = Shop("Ibrahim")
# print(shoping.add_cart("Mobile", 4000, 1))
shoping.add_cart("Mobile", 4000, 1)
shoping.add_cart("laptop", 40000, 1)
shoping.add_cart("watch", 2000, 3)
print(shoping.cart)
shoping.checkout(300000)
