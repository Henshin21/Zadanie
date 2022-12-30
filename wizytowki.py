class BaseContact():
    def __init__(self, name, surname, number, email):
        self.name = name
        self.surname = surname
        self.number = number
        self.email = email

    def contact():
        print(f"Wybieram numer {number} i dzownie do {name} {surname}")

class BusinessContact(BaseContact):
    def __init__(self, position, company, business_number):
        super().__init__(name, surname, email)
        self.position = position
        self.company = company
        self.business_number = business_number

    def contact():
        print(f"Wybieram numer {business_number} i dzownie do {name} {surname}")
    
    @property
    def label_lenght():
        return len(self.name, self.surname)

def create_contacts():
    
