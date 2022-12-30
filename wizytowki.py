from faker import Faker

fake = Faker()

class BaseContact():
    def __init__(self, name, surname, number, email):
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.number} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return len(self.name + self.surname)

class BusinessContact(BaseContact):
    def __init__(self, name, surname, number, email, position, company, business_number):
        super().__init__(name, surname, number, email)
        self.position = position
        self.company = company
        self.business_number = business_number

    def contact(self):
        print(f"Wybieram numer {self.business_number} i dzwonię do {self.name} {self.surname} ({self.position} w {self.company})")
    
    @property
    def label_length(self):
        return len(self.name + self.surname)

def create_contacts(contact_type, amount):
    if contact_type == "base":
        return [BaseContact(fake.first_name(), fake.last_name(),fake.phone_number(),fake.email()) for x in range(amount)]
    elif contact_type == "Business":
        return [BusinessContact(fake.first_name(), fake.last_name(),fake.phone_number(),fake.email(), fake.job(), fake.company(), fake.phone_number()) for x in range(amount)]

contacts = create_contacts("business", 4)
for contact in contacts:
    contact.contact()
print(create_contacts("business", 4))
