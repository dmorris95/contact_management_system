Welcome to the Contact Management System!
https://github.com/dmorris95/contact_management_system


This application allows for users to have a single place to hold all of their contacts in an orderly fashion in a single file
Contact information is held in a dictionary with a key identifier of their phone number. The information the dictionary contains is the contacts name, phone number, email, address, and notes about the contact

1. Adding a contact
When a adding a contact the information needs to be put in a logical format and no fields can be left empty.
For example phone numbers must be in the XXX-XXX-XXXX format. 
Emails must also be in a logical format. The format aaaa@zzzz.com will work but an email without the @ and . will not work
Phone numbers must be unique as they are the key identifier for the contact

2. Editing Contacts
For editing contacts there must first be at least 1 contact in the holding dictionary.
It prompts the user to enter the phone number of the contact they wish to edit. 
It then gives the user the list of the details the user is able to edit.
If the user chooses to edit the phone number it will also modify their key identifier

3. Deleteing Contacts
When this is selected it prompts the user if they have no contacts in the dictionary. If the dictionary is populated it prompts the user for the phone number of the contact they would like to delete.

4. Searching Contacts
When selected it also prompts the user if the dictionary is without contacts.
It allows the user to display the full details of a contact based on their input of the phone number.

5. Display Contacts
Displays the contacts of the dictionary. It only shows their key identifier and the name of the contact

6. Exporting Contacts
Takes the dictionary of contacts and puts it into a text file.
It formats the details of the contacts so its easy to read.

7. Importing Contacts
Imports contacts from the text file and then puts them into the dictionary. 

8. Quit
Quits the program and displays an exit message

