from faker import Faker

fake = Faker()

class BaseContact():
    def __init__(self, name, surname, number, email):
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.number} i dzownie do {self.name} {self.surname}")

class BusinessContact(BaseContact):
    def __init__(self, name, surname, number, email, position, company):
        super().__init__(name, surname, number, email)
        self.position = position
        self.company = company

    def contact(self):
        print(f"Wybieram numer {self.number} i dzownie do {self.name} {self.surname}({self.postion} w {self.comapny})")
    
    @property
    def label_lenght(self):
        return len(self.name + self.surname)

def create_contacts(contact_type, amount):
    if contact_type == "base":
        return [BaseContact(fake.first_name(), fake.last_name(),fake.number(),fake.email()) for x in range(amount)]
    elif contact_type == "Business":
        return [BusinessContact(fake.first_name(), fake.last_name(),fake.number(),fake.email(), fake.position(), fake.company()) for x in range(amount)]
    else:
        return []


contacts = create_contacts("business", 4)

