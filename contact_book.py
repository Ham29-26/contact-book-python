import os

user_input = ""
user_contact = {}

if os.path.exists("contacts.txt"):
    with open("contacts.txt", "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 3:
                name_part = parts[0].split(": ")[1].lower()
                phone_part = parts[1].split(": ")[1]
                email_part = parts[2].split(": ")[1]
                user_contact[name_part] = (phone_part, email_part)

def search(username):
    username = username.lower()
    if username in user_contact:
        user_phone, user_email = user_contact[username]
        print(f"\n--- Contact Details of {username} ---")
        print("Phone:", user_phone)
        print("Email:", user_email)
    else:
        print(f"\nSorry, {username} not found in the contacts.")


while user_input != 'q':
    print("\n--- Contact Book ---")
    print("Type a to add a contact")
    print("Type v to view all contact details")
    print("Type s to search a particular contact: ")
    print("Type q to exit the portal")

    user_input = input("\nEnter a prompt: ")

    if user_input == 'a':
        name = input("\nEnter name: ").lower()
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        user_contact[name] = (phone, email)  # <- Now it stores a tuple

        with open("contacts.txt", "a") as file:
            file.write("Name: " + name + " | " + "Phone: " + phone + " | " + "Email: " + email + "\n")

        print("\nContact Saved!")


    elif user_input == 'v':
        with open("contacts.txt", "r") as file:
            content = file.read()
            print("\n--- Contact Details ---")
            print(content)


    elif user_input == 's':
        nameSearched = input("Enter a name to search: ")
        search(nameSearched)


    elif user_input == 'q':
        print("\nExiting Portal.....")
        break


    else:
        print("\nInvalid input! Please try again.")
