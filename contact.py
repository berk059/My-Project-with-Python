import sys

# Keys used for each contact dictionary entry
CONTACT_KEYS = ('name','phone','email','country')

# Menu items that will be shown to the user
MENU_OPTIONS = {
        '1': "Add New Contact",
        '2': "View All Contacts",
        '3': "Edit Contact",
        '4': "Delete Contact",
        '5': "Exit"
    }

# This function prints the main menu for user
def display_main_menu():
        """Ana menüyü ekrana yazdırır"""
        print("\n--- MAIN MENU ---")
        for key, value in MENU_OPTIONS.items():
            print(f"{key}. {value}")
        print("------------------")

# This function adds a new contact
def add_contact(contacts):
        name = input("Enter Name:")
        phone = input("Enter Phone:")
        email = input("Enter Email:")
        country = input("Enter Country:")

        # Name cannot be empty
        if name =="":
            print("Error: Name is required.")
            return False

        # Phone must be 11 numeric digits
        if len(phone) != 11:
            print("Error: Phone must be 11 digits.")
            return False
        for number in phone:
            if not number.isdigit():
                print("Error: Phone number must consist only of numbers.")
                return False

        # Email and country cannot be empty
        if email == "":
            print("Error: Email is required.")
            return False
        if country == "":
            print("Error: Country is required.")
            return False

        # Create the contact dictionary and append to list
        contact = {'name':name,'phone':phone,'email':email,'country':country}
        contacts.append(contact)
        print("Success :","Contact",name,"added.")
        return True

# This function displays all contacts in formatted list
def view_contacts(contacts):
        print("--- CONTACT LIST ---")
        if len(contacts) == 0:
            print("No contacts found.")
            return False

        # Print header
        header = "Index | "
        for KEY in CONTACT_KEYS:
            header = header + KEY.capitalize() + "   |"

        print(header)
        print("---------------------------------------------------------")

        # Print each contact with its index
        for contact in contacts:
            index = contacts.index(contact)+1
            name = contact['name']
            phone = contact['phone']
            email = contact['email']
            country = contact['country']
            print(index,"   |",name,"   |",phone,"   |",email,"   |",country)

# This function edits existing contact chosen by the user
def edit_contact(contacts):
        print("--- EDIT CONTACT ---")
        name = input("Enter the name (or part of the name) of the contact to edit or type 'cancel' to return to menu:")
        matches =[]
        selected_contacts =[]

        # Cancel option
        if name == "cancel" :
             return False

        # Search for matching names
        for i in range(len(contacts)):
            if name.lower() in contacts[i]['name'].lower():
                matches.append(i)

        # If no matches found
        if len(matches) == 0:
            print("No matches found.")
            return False

        # Exactly one match found
        if len(matches) == 1:
            print("Only one match found.")
            real_index = matches[0]

        # Multiple matches found, user must choose one
        elif len(matches) > 1:
            print("Multiple contacts found. Please select one to edit:")
            num = 1
            for i in matches:
                selected_contacts.append(contacts[i])
                name = contacts[i]['name']
                print("["+str(num)+"]" + name)
                num += 1
            choice = input("Enter number of contact to edit:")
            real_index = matches[int(choice)-1]

        print("Editing contact: " + contacts[real_index]["name"])
        print( "Which field do you want to change?")
        selected_contact = contacts[real_index]

        # Show current values
        print("1: Name "+"(Current: "+selected_contact['name']+".)")
        print("2: Phone "+"(Current: "+selected_contact['phone']+".)")
        print("3: Email "+"(Current: "+selected_contact['email']+".)")
        print("4: Country "+"(Current: "+selected_contact['country']+".)")

        # User selects which field to edit
        field_choice = input("Enter choice (1-4):")
        if field_choice == "0":
            print("Exiting...")
            return False

        # Update selected field
        elif field_choice == "1":
            selected_contact['name'] = input("Enter new value for Name:")
            print("Success! Name updated for " + selected_contact['name'])
        elif field_choice == "2":
            selected_contact['phone'] = input("Enter new value for Phone:")
            print("Success! Phone updated for " + selected_contact['name'])
        elif field_choice == "3":
            selected_contact['email'] = input("Enter new value for Email:")
            print("Success! Email updated for " + selected_contact['name'])
        elif field_choice == "4":
            selected_contact['country'] = input("Enter new value for Country:")
            print("Success! Country updated for " + selected_contact['name'])

# This function deletes an existing contact after user confirmation
def delete_contact(contacts):
            print("--- DELETE CONTACT ---")
            name = input("Enter the name (or part of the name) of the contact to delete:")

            # Allow user to cancel
            if name == "cancel" :
                return False

            # Search for matching contacts
            matches = []
            for i in range(len(contacts)):
                if name.lower() in contacts[i]['name'].lower():
                    matches.append(i)

            # No match found
            if len(matches) == 0:
                print("No matches found.")
                return False

            # One match found
            elif len(matches) == 1:
                print("Only one match found.")
                real_index = matches[0]
                selected_contact = contacts[real_index]

            # Multiple matches , user must choose
            else:
                print("Multiple contacts found. Please select one to delete:")
                num = 1
                for i in matches:
                    contact = contacts[i]
                    print("[" + str(num) + "] " + contact['name'] + " (" + contact['phone'] + ")")
                    num += 1
                choice = input("Enter number of contact to delete, or type 0 to cancel:")

                # Cancel option
                if int(choice) == 0:
                    print("Deletion cancelled.")
                    return False

                real_index = matches[int(choice)-1]
                selected_contact = contacts[real_index]

            # Ask for final confirmation
            answer = input("Are you sure you want to delete " + (selected_contact['name']) + "? (yes/no):")

            # Delete if confirmed
            if answer.lower() == "yes":
                    contacts.pop(real_index)
                    print("Successfully deleted " + str(selected_contact['name']))
                    return True
            elif answer.lower() == "no":
                    print("Deletion cancelled.")
                    return False

# This function runs the menu loop until the user chooses to exit
def run_manager(contacts):
        while True:
            display_main_menu()
            choice = input("Enter your choice(1-5): ")

            if choice == "1":
                    add_contact(contacts)
            elif choice == "2":
                    view_contacts(contacts)
            elif choice == "3":
                    edit_contact(contacts)
            elif choice == "4":
                     delete_contact(contacts)
            elif choice == "5":
                    print("Exiting Contact Manager  ...")
                    break
            else:
                    print("Invalid choice. Please try again.")

# This block checks if script is run directly.
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        try:
            sys.stdin = open(input_file_path, 'r')
        except FileNotFoundError:
            sys.exit(1)

    contacts_list = []
    run_manager(contacts_list)

    if len(sys.argv) > 1:
        sys.stdin.close()
