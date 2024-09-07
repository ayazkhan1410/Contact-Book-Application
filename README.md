## Contact Book Application in Python

This is a simple Contact Book application written in Python that allows users to manage their contacts via a console-based menu. It supports basic operations such as creating, viewing, searching, updating, and deleting contacts.

### Features

1. **Check Total Contacts**: View the total number of contacts saved in the contact book.
2. **Create Contact**: Add a new contact with details like name, age, email, and phone number.
3. **View Contacts**: Display all saved contacts in the contact book.
4. **Search Contact**: Search for a contact by name and display the contact details if found.
5. **Update Contact**: Update the details (age, email, phone number) of an existing contact.
6. **Delete Contact**: Delete a contact by name from the contact book.
7. **Exit Program**: Exit the application.

### How to Use

1. Run the Python script to start the Contact Book program.
2. Follow the menu displayed in the console to choose an action.
3. Enter the appropriate number (0-7) to select a menu option.
4. Input the required details when prompted, such as the name, age, email, or phone number.
5. The program will execute the chosen action and display the relevant information or confirmation message.

### Menu Options

- **0. Check Total Contacts**: Displays the total number of contacts currently saved.
- **1. Create Contact**: Prompts for the contact details and adds a new contact to the book.
- **2. View Contacts**: Lists all the contacts with their details.
- **4. Search Contact**: Asks for the contact name and searches for it in the contact book.
- **5. Update Contact**: Prompts for the name of the contact to update and the new details.
- **6. Delete Contact**: Deletes the specified contact from the book.
- **7. Exit Program**: Closes the application.

### Example Usage

```plaintext
Welcome to Contact Book
0. Check Total Contacts
1. Create Contact
2. View Contacts
4. Search Contact
5. Update Contact
6. Delete Contact
7. Exit Program
Choose: 1

Enter name: John Doe
Enter age: 30
Enter email: john@example.com
Enter Phone Number: 1234567890
-----------------------------
Contact saved ...
-----------------------------
```

### Error Handling

- The program includes error handling for invalid inputs, such as non-integer values for age or invalid menu choices.
- If an exception occurs, it will display the error message to the user.

### Requirements

- Python 3.x

### Running the Application

1. Save the code in a file named `contact_book.py`.
2. Run the script using a Python interpreter:
    ```bash
    python contact_book.py
    ```

### Contributing

Feel free to fork this project, submit issues, and send pull requests if you'd like to contribute!

### License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). 

### Acknowledgments

This application is intended for educational purposes and serves as a simple demonstration of how to use Python for console-based CRUD operations.
