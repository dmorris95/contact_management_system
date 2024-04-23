'''
Contact Structure:

        {phone number: {name: "", phone number: "", email: "", address: "", notes ""}}

'''
contact_dict = {}
import re

#Display Menu Function
def display_menu(c_dict):
    menu_choice = 0
    menu_options = "1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Import contacts from a text file\n8. Quit"
    try:
        while menu_choice != 8:
            print(f"Welcome to the Contact Management System!\nMenu:\n{menu_options}")
            menu_choice = menu_input(c_dict)
    except PermissionError:
        print("error")
    finally:
        print("Thank you for using the contact management system!")

#Function that takes users input and performs the correct function
def menu_input(c_dict):
    try:
        user_input = int(input('Please choose a number to continue: '))
        if user_input > 0 and user_input < 9:
            if user_input == 1:
                add_contact(c_dict)
            elif user_input == 2:
                edit_contact(c_dict)
            elif user_input == 3:
                delete_contact(c_dict)
            elif user_input == 4:
                search_contact(c_dict)
            elif user_input == 5:
                display_contacts(c_dict)
            elif user_input == 6:
                export_contacts(c_dict, "finished_contact_list.txt")
            elif user_input == 7:
                import_contacts("contacts.txt", c_dict)
            else:
                return user_input
        else:
            raise ValueError()
    except ValueError:
        print("You must select a number between 1 and 8.")

#Function that allows for the user to add a new contact.
def add_contact(contacts):
    phone_pattern = r"\d{3}-\d{3}-\d{4}"
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]"

    try:
        key_input = input("Please enter the contacts phone number: ")
        while True or key_input in contacts:
            if key_input in contacts:
                key_input = input("This person is already in your contacts!\nPlease enter a different phone number: ")
            else:    
                if re.match(phone_pattern, key_input):
                    break
                else:
                    key_input = input("You must enter the phone number in the format XXX-XXX-XXXX: ")
        
        #Name input validation
        name_input = input("Please enter the name of the contact: ")
        while name_input == "":
            name_input = input("Name can not be blank, please enter the contacta name: ")

        #Email input validation
        email_input = input("Please enter the contacts email: ")
        while True:
            if re.match(email_pattern, email_input):
                break
            else:
                email_input = input("The email must follow the appropriate format\nPlease try again: ")

        #Address input validation
        address_input = input("Please enter the contacts address: ")
        while True:
            if address_input == "":
                address_input = input("You must enter an address for the contact: ")
            else:
                break    
        
        #Note input validation
        notes_input = input("Please enter somes notes about the contact: ")
        while True:
            if notes_input == "":
                notes_input = input("You must enter some notes about the contact\nPlease enter some notes about the contact: ")
            else:
                break

        #once all information has been validated add contact to dictionary
        contacts[key_input] = {"Name": name_input, "Phone Number": key_input, "Email": email_input, "Address": address_input, "Notes": notes_input}
        print("Contact has been successfully added!")
    except:
        print("An error occured, please try again!")
    
    finally:
        display_menu(contacts)



#Function that allows for editing of a contacts details
def edit_contact(contacts):
    phone_pattern = r"\d{3}-\d{3}-\d{4}"
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]"

    #Check for empty contact dictionary
    if len(contacts) == 0:
        print("You must have some contacts first! Try adding some or importing from a file.")
    else:
        try:
            num_input = input("Please enter the phone number of the contact you would like to edit: ")
            while True:
                if num_input in contacts:
                    print("What information would you like to edit:\n1. Name\n2. Phone Number\n3. Email\n4. Address\n5. Notes\n6. Cancel")
                    user_choice = int(input("Please type the number of the option you would like to edit: "))

                    changed_info = ""
                    if user_choice > 0 and user_choice < 6:
                        if user_choice == 1:
                            print(f"Current Name: {contacts[num_input]["Name"]}")
                            changed_info = input("What would you like to change the name to: ")
                            while changed_info == "":
                                changed_info = input("You can't leave the name blank!\nPlease try again: ")
                            contacts[num_input].update({"Name": changed_info})

                        elif user_choice == 2:
                            print(f"Current Phone Number: {contacts[num_input]["Phone Number"]}")
                            changed_info = input("Please enter the contacts new phone number: ")
                            while True:
                                if changed_info in contacts:
                                    changed_info = input("This number is already in your contacts please enter a different phone number: ")
                                else:
                                    if re.match(phone_pattern, changed_info):
                                        contacts[changed_info] = contacts.pop(num_input)
                                        contacts[changed_info].update({"Phone Number": changed_info})
                                        
                                    else:
                                        changed_info = input("The phone number must be in the XXX-XXX-XXXX format, please try again: ")

                        elif user_choice == 3:
                            print(f"Current Email: {contacts[num_input]["Email"]}")
                            changed_info = input("Please enter the contacts new email: ")
                            while True:
                                if re.match(email_pattern, changed_info):
                                    contacts[num_input].update({"Email": changed_info})
                                else:
                                    changed_info = input("Contacts email must be entered in the proper format.\nPlease enter the contatcs email: ")

                        elif user_choice == 4:
                            print(f"Current Address: {contacts[num_input]["Address"]}")
                            changed_info = input("Please enter the contacts new address: ")
                            while changed_info == "":
                                changed_info = input("Contacts address can't be empty!\nPlease enter the contacts new address: ")
                            contacts[num_input].update({"Address": changed_info})
                            
                        elif user_choice == 5:
                            print(f"Current Notes for {contacts[num_input]["Name"]}: {contacts[num_input]["Notes"]}")
                            changed_info = input("Please enter the new notes: ")
                            while changed_info == "":
                                changed_info = input("Notes can't be left blank!")
                            contacts[num_input].update({"Notes": changed_info})
                    else:
                        break #when user chooses 6 it cancels the edit
                else:
                    num_input = input("That phone number is not in your contacts, please try again: ")
        except ValueError:
            print("You must enter a number between 1 and 6.")
        finally:
            display_menu(contacts)


#Function that deletes a contact based on the phone number that is entered.
def delete_contact(contacts):
    #Check for an empty contact list
    if len(contacts) == 0:
        print("You must have some contacts first! Try adding some or importing from a file.")
    else:
        num_del = input("Please enter the phone number of the contact you would like to delete: ")
        try:
            if num_del in contacts:
                del contacts[num_del]
                print("Contact has been successfully deleted.")
            else:
                print("That number is not in your contacts. Please try again")
        except:
            print("An error has occured, please try again!")
        finally:
            display_menu(contacts)

#Function that allows the user to search for the Contact based on their phone number and shows all details related to the contact
def search_contact(contacts):
    #First check for empty contact list
    if len(contacts) == 0:
        print("You must have some contacts first! Try adding some or importing from a file.")
    else:
        num_search = input("Please enter the phone number of the contact you would like to view: ")
        try:
            if num_search in contacts:
                #Loop through dictionary to find contact
                for c_num, c_data in contacts.items():
                    if (c_num) == num_search:
                        print(f"Contact Number: {c_num}\nName: {c_data["Name"]}\nPhone Number: {c_num}\nEmail: {c_data["Email"]}\nAddress: {c_data["Address"]}\nNotes: {c_data["Notes"]}")
            else:
                print("The entered phone number is not one of your contacts. Please try again!")
        except:
            print("An error has occured, please try again!")


#Function that displays the phone number and the name of the contact
def display_contacts(contacts):
    if len(contacts) == 0:
        print("You must have some contacts first! Try adding some or importing from a file.")
    else:
        for contact_num, contact_data in contacts.items():
            print("Phone Number:", contact_num, "---------- Contact Name:",contact_data["Name"])


#Function that exports the contact dictionary into the given file.
def export_contacts(contacts, filename):
    if len(contacts) == 0:
        print("You must have some contacts first! Try adding some or importing from a file.")
    else:
        #Run try/except to export contact dictionary.
        try:
            with open(filename, 'w') as file:
                for key_phone, contact_data in contacts.items():
                    file.write(f"Key Identifier: {key_phone}\nName: {contact_data["Name"]} ------ Phone Number: {contact_data["Phone Number"]}\nEmail: {contact_data["Email"]}\nAddress: {contact_data["Address"]} -------- Notes: {contact_data["Notes"]}\n\n")
                print("Contacts has been successfully exported to the file!")
        except FileNotFoundError:
            print("File not found please try again!")
        

#Function that imports contacts from the given file
def import_contacts(filename, contacts):
    try:
        with open(filename, 'r') as file:
            
            for line in file:
                phone, name, p_num, email, address, notes = line.strip().split(',')
                contacts[phone] = {"Name": name, "Phone Number": p_num, "Email": email, "Address": address, "Notes": notes}
            
    except FileNotFoundError:
        print("The file could not be located")
    finally:
        print("File successfully imported!")
        display_menu(contacts)

#Run Program
display_menu(contact_dict)