contacts = {}

# Function to add a contact
def add_contact(name, phone):
    if name in contacts:
        print(f"Contact '{name}' already exists.")
    else:
        contacts[name] = phone
        print(f"Contact '{name}' added successfully.")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

# Function to update a contact's phone number
def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Function to delete a contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Function to display all contacts
def display_contacts():
    if contacts:
        print("Contact List:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")

# Main function to drive the program
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            update_contact(name, phone)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
