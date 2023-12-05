class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        found = []
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                found.append(contact)
        return found

    def update_contact(self, contact_index, updated_contact):
        self.contacts[contact_index] = updated_contact
        print("Contact updated successfully.")

    def delete_contact(self, contact_index):
        del self.contacts[contact_index]
        print("Contact deleted successfully.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(search_term)
            if found_contacts:
                print("Search results:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            contact_book.view_contacts()
            contact_index = int(input("Enter the index of contact to update: ")) - 1
            updated_name = input("Enter updated name: ")
            updated_phone_number = input("Enter updated phone number: ")
            updated_email = input("Enter updated email: ")
            updated_address = input("Enter updated address: ")
            updated_contact = Contact(updated_name, updated_phone_number, updated_email, updated_address)
            contact_book.update_contact(contact_index, updated_contact)

        elif choice == '5':
            contact_book.view_contacts()
            contact_index = int(input("Enter the index of contact to delete: ")) - 1
            contact_book.delete_contact(contact_index)

        elif choice == '6':
            print("Thank you for using the Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
