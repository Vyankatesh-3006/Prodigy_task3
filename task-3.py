contact ={}

def display_contact():
    print("name\t\tcontact_number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    
    choice =int (input(" 1.Add new contact \n 2.Search contact \n 3.Display contact\n 4.Edit contact\n 5.Delete contact\n 6.Exit\n Enter your choice :"))
    
    if choice==1:
        name=input("Enter the name:")
        phone=input ("Enter the number:")
        contact[name]=phone
    
    elif choice==2:
        search_name =input (" Enter the name you want to search:")
        if search_name in contact:
            print( search_name," contact number is", contact [search_name])
        else:
            print(" The name is not found")
    
    elif choice==3:
        if not contact:
            print("  The contact list is empty")
        else:
            display_contact()
            
    elif choice==4:
        edit_contact=input(" Enter the contact to be edited :")
        if edit_contact in contact:
            phone =input(" Enter the   edited mobile number:")
            contact[edit_contact]=phone
            print(" contact updated")
            display_contact()
        else:
            print(" Name is not found in contact book")
    
    elif choice==5:
        delete_contact=input(" Enter the  contact to be deleted:")
        if delete_contact in contact:
            confirm=input(" Do you want to delet the contact y/n :")
            if confirm=='y':
               contact.pop (delete_contact)
               display_contact()
            else:
                print(" The name is not found in contact book")
    else:
        break             

