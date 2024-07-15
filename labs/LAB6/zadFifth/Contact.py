

class Contact:
    def __init__(self, name, last_name, email, phone):
        self.name = name
        self.last_Name = last_name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'Name: {self.name} Last Name: {self.last_Name} Email: {self.email} phone: {self.phone}'



