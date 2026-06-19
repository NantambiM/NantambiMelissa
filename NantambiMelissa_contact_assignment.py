import re
import sys
def add_contact():
    print(1)

def view_contact():
    print(2)

def update_contact():
    print(3)

def delete_contact():
    print(4)

def search_contact():
    print(5)

def list_all_contacts():
    print(6) 

telephone=""

def validate_contact(contact):
    pattern=r"[+]\d{3}-\d{9}"
    if re.match(pattern,contact):
        global telephone
        telephone=contact
    else:
        telephone=""
        print("Error: Invalid contact format")
    return telephone

print(validate_contact("+256-786060966"))

user_email=""

def validate_email(email):
    pattern=r"^[a-zA-Z0-9._%=-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern,email):
        global user_email
        user_email=email
    else:
        email=""
        print("Error: Invalid email format")
    return user_email

print(validate_email("sdfghjk@g.dfg"))

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    if validate_contact(phone) == "":
        return

    if email != "" and validate_email(email) == "":
        return

    # ContactManager.add_contact(name, phone, email)
    print("Contact added.")

def search_contact():

    term = input("Enter name, phone or email to search: ")

    # search(contact_manager.contacts, term)

def search(contacts_list, search_term):

    results = []

    for contact in contacts_list:

        if (search_term.lower() in contact[0].lower()
            or search_term in contact[1]
            or search_term.lower() in contact[2].lower()):

            results.append(contact)

    if len(results) == 0:
        print("No contacts found.")
        return

    print("\n===== Search Results =====")

    for contact in results:
        print(f"Name : {contact[0]}")
        print(f"Phone: {contact[1]}")
        print(f"Email: {contact[2]}")
        print("------------------------")
    results = []

    for contact in contacts_list:
        name = contact[0]
        phone = contact[1]
        email = contact[2]

        # Search by name, phone, or email
        if (search_term.lower() in name.lower() or
            search_term in phone or
            search_term.lower() in email.lower()):
            results.append(contact)

    # Display results nicely
    if results:
        print("\n===== Search Results =====")
        for i, contact in enumerate(results, start=1):
            print(f"Contact {i}")
            print(f"Name : {contact[0]}")
            print(f"Phone: {contact[1]}")
            print(f"Email: {contact[2]}")
            print("-" * 25)
    else:
        print("No matching contacts found.")

def main():

    actions={
        "1":add_contact,
        "2":view_contact,
        "3":update_contact,
        "4":delete_contact,
        "5":search_contact,
        "6":list_all_contacts
    }
    while True:
        choice=input("""=== Contact Manager Menu ===
        1. Add Contact
        2. View Contact
        3. Update Contact
        4. Delete Contact
        5. Search Contacts
        6. List All Contacts
        7. Exit
        Choose an option (1-7):  
        """)
        
        if choice=="7":
            print('''
                  See you next time!
                  ''')
            break
        
        if choice not in actions:
            print('''
                  Invalid choice. Try again!
                  ''')
        else:
            actions[choice]()

main()