class Phone:
    manufacturer = "Bangladesh"

    def __init__(self, name, title, color, price):
        self.name = name
        self.title= title
        self.color=color
        self.price=price


my_phone = Phone("Nova 3i","best Huwaei phone","Blue",12000)

print(my_phone.name,my_phone.manufacturer)
