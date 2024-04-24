# Class

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init user object
aisyah = User('Haryati Astuti', 'astuti@gmail.com', 20)
# Init customer object
atan = Customer('Ahyar Pattani', 'pattani@yahoo.com', 19)

atan.set_balance(500)
print(atan.greeting())

aisyah.has_birthday()
print(aisyah.greeting())