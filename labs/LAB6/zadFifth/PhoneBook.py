import json
import pickle

from labs.LAB6.zadFifth.Contact import Contact


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def addContact(self, contact):
        self.contacts.append(contact)

    def removeContact(self, contact):
        self.contacts.remove(contact)

    def getContacts(self):
        return self.contacts

    def printContacts(self):
        for contact in self.contacts:
            print(contact)

    def printContact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)

    def write_contacts(self):
        contacts_list = [{'name': contact.name, 'last_name': contact.last_Name, 'email': contact.email, 'phone': contact.phone} for contact in self.contacts]
        with open('./contacts.json', 'w') as contacts_file:
            json.dump(contacts_list, contacts_file, indent=4)

    def read_contacts(self):
        with open('./contacts.json', 'r') as contacts_file:
            contacts_data = json.load(contacts_file)
            self.contacts = [Contact(contact['name'], contact['last_name'], contact['email'], contact['phone']) for contact in contacts_data]



# contact1 = Contact("Emily", "Smith", "emilysmith@example.com", "123456789")
# contact2 = Contact("Michael", "Johnson", "michaeljohnson@gmail.com", "123456789")
# contact3 = Contact("Emma", "Williams", "emmawilliams@microsoft.com", "123456789")
# contact4 = Contact("Sophia", "Jones", "sophiajones@yahoo.com", "123456789")

phoneBook = PhoneBook()
# phoneBook.addContact(contact1)
# phoneBook.addContact(contact2)
# phoneBook.addContact(contact3)
# phoneBook.addContact(contact4)

phoneBook.printContacts()
phoneBook.printContact("Emily")

#phoneBook.write_contacts()


phoneBook.read_contacts()
phoneBook.printContacts()