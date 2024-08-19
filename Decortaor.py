class User:
    def __init__(self, f_name, L_name):
        self.first_name = f_name,
        self.last_name = L_name,
        self.email = f'{f_name}{L_name}@gmail.com'


Biplob = User('mdibrahim', 'biplob')
print(Biplob.first_name)
print(Biplob.last_name)
print(Biplob.email)
