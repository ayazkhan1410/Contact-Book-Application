class ContactBook:
    contacts = {}
    no_of_contacts = 0 
    
    def menu(self):
        print("0. Check Total Contacts")
        print("1. Create Contact")
        print("2. View Contacts")
        print("4. Search Contact")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit Program")
        choice = int(input("Choose: "))
        return choice
    
    def total_contacts(self):
        if self.no_of_contacts == 0:
            print("-----------------------------")
            print("No contact found")
            print("-----------------------------")
        else:
            print("Total Contacts: ", self.no_of_contacts)
    
    def create_contact(self):
        try:
            name = input("Enter name: ").lower()
            if name in self.contacts:
                print(f"Contact with name {name} already exsists")
            else:
                age = int(input("Enter age: "))
                email = input("Enter email: ")
                phone_number = input('Enter Phone Number: ')
                self.contacts[name] = {'age':age,'email':email,'phone_number':phone_number }
                print("-----------------------------")
                print("Contact saved ...")
                print("-----------------------------")
                self.no_of_contacts+=1
        except Exception as e:
            print(e)
            
    def view_contacts(self):
        if self.no_of_contacts == 0:
            print("-----------------------------")
            print("No Contact to show")
            print("-----------------------------")
        for name,info in self.contacts.items():
            print(f"{name} - {info}")
        
    def search_contact(self):
        name = input("Enter name to search: ").lower()
        if not name in self.contacts:
            print("-----------------------------")
            print("Contact Not Found")
            print("-----------------------------")
        else:
            search_contact = self.contacts[name]
            print("-----------------------------")
            print("Contact Found ")
            print(f" Name: {name}  Age:{search_contact['age']} Email:{search_contact['email']} PhoneNumber: {search_contact['phone_number']}")
            print("-----------------------------")
    
    def update_contact(self):
        try:
            name = input("Enter Name to Update Contact: ")
            if not name in self.contacts:
                print(f"No Contact Found with this '{name}' name")
            else:
                age = int(input("Enter age: "))
                email = input("Enter email: ")
                phone_number = input('Enter Phone Number: ')
                self.contacts[name] = {'Age':age,'Email':email,'Phone Number':phone_number}
                print("-----------------------------")
                print("Contact Update Successfully ...")
                print("-----------------------------")
        except Exception as e:
            print(e)
            
    def delete_contact(self):
        try:
            name = input("Enter Contact name to delete: ")
            if not name in self.contacts:
                print("-----------------------------")
                print(f"No Contact Found with this '{name}' name")
                print("-----------------------------")
            else:
                del self.contacts[name]
                self.no_of_contacts -=1
                print("-----------------------------")
                print("Contact has been deleted Successfully")
                print("-----------------------------")
        except Exception as e:
            print(e)
                    
def main():
    cc = ContactBook()
    while True:
        result = cc.menu()
        try: 
            if result == 0:
                cc.total_contacts()
            elif result == 1:
                cc.create_contact()
            elif result == 2:
                print("Saved Contacts:")
                cc.view_contacts()    
            elif result == 4:
                cc.search_contact()
            elif result == 5:
                cc.update_contact()
            elif result == 6:
                cc.delete_contact()
            elif result == 7:
                break
            else:
                print("-----------------------------")
                print("Please Choose Valid Number")
                print("-----------------------------")
        except Exception as e:
            print(e)
            
    print("-----------------------------")
    print("Thank You for using our program")
    print("-----------------------------")

if __name__ == "__main__":
    main()