class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Jack(Person):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self. balance = balance
    def pr(self):
        print(f"{self.balance}")

class Vito(Jack):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)
    def g(self):
        self.balance += n
        jack.balance -= n
    def pr(self):
        print(f"{self.balance}")
n = 2
vito = Vito('Lol', 'Dol', '0555 676 432', 12 )
jack = Jack('Hol', 'Mol', '0999 887 665', 10)
vito.g()
jack.pr()
vito.pr()

