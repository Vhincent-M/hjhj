import csv 
import os

def load_contacts(filename):

    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("Contacts file not found. Creating a new one.")
        return []

def save_contacts(filename, contacts):

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(contacts)

def display_contacts(contacts):
    print("\n{:<20} {:<15} {:<30}".format("Name", "Phone", "Email"))
    print("-" * 65)
    for contact in contacts:
        print("{:<20} {:<15} {:<30}".format(contact['Name'], contact['Phone'], contact['Email']))

def remove_duplicates(filename):
    if not os.path.exists(filename):
        print("No contacts found.")
        return

    contacts = load_contacts(filename)
    seen = set()
    duplicates = []
    unique_contacts = []

    for contact in contacts:
        # Only check Name and Phone for duplicates, ignoring Email
        contact_tuple = (contact["Name"].strip(), contact["Phone"].strip())

        if contact_tuple in seen:
            duplicates.append(contact_tuple)
        else:
            seen.add(contact_tuple)
            unique_contacts.append(contact)

    if duplicates:
        print("\nDuplicate Contacts Found (based on Name & Phone):")
        for dup in duplicates:
            print(f"- {dup[0]} | {dup[1]}")

        save_contacts(filename, unique_contacts)  # Save cleaned contacts
        print("\n✅ Duplicates removed successfully!")
    else:
        print("\n✅ No duplicate contacts found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['Name'].lower() == name.lower():
            contacts.remove(contact)
            print(f"Contact '{name}' deleted successfully.")
            return
    print("Contact not found.")

def run_contact_manager():

    filename = 'contacts.csv'
    
    while True:
        print("\nContact Manager")
        print("1. Display Contacts")
        print("2. Add a Contact")
        print("3. Update a Contact")
        print("4. Delete a Contact")
        print("5. Find and Remove Duplicates")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            contacts = load_contacts(filename)
            display_contacts(contacts)
        elif choice == '2':
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            email = input("Enter email: ").strip()
            contacts = load_contacts(filename)
            contacts.append({"Name": name, "Phone": phone, "Email": email})
            save_contacts(filename, contacts)
            print("\n✅ Contact added successfully!")
        elif choice == '3':
            contacts = load_contacts(filename)
            name = input("Enter the name of the contact to update: ").strip()
            found = False
            for contact in contacts:
                if contact["Name"].lower() == name.lower():
                    contact["Phone"] = input(f"Enter new phone for {name}: ").strip()
                    contact["Email"] = input(f"Enter new email for {name}: ").strip()
                    found = True
                    print("\n✅ Contact updated successfully!")
                    break
            if not found:
                print("\n❌ Contact not found.")
            save_contacts(filename, contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(filename, contacts)
        elif choice == '5':
            remove_duplicates(filename) 
        elif choice == '6':
            print("\nGoodbye! 👋")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")

run_contact_manager()