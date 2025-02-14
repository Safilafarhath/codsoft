contacts = {}
def add():
    name=input("Enter name:")
    if name in contacts:
        print("Contact already exists.")
        return
    phone=input("Enter ph.no:")
    email=input("Enter email:")
    address=input("Enter address:")
    contacts[name]={"phone":phone,"email":email,"address":address}
    print("Contact added successfully")
def view():
    if not contacts:
        print("contacts can't found")
        return
    print("\nContact List:")
    for name,details in contacts.items():
        print(f"{name}-Phone:{details['phone']}")
def search():
    search=input("Enter name to search: ")
    for name,details in contacts.items():
        if search.lower() in name.lower() or search == details["phone"]:
            print(f"\nContact Found:\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
            return
    print("Contact can't found")
def update():
    name = input("Enter contact name to update:")
    if name in contacts:
        print("What you want to update?")
        print("1.Phone\n2.Email\n3.Address")
        choice = input("Enter your choice:")
        if choice == '1':
            contacts[name]["phone"]=input("Enter new phone number:")
        elif choice == '2':
            contacts[name]["email"]=input("Enter new email:")
        elif choice == '3':
            contacts[name]["address"]=input("Enter new address:")
        else:
            print("Invalid choice.")
            return
        print("Contact updated successfully")
    else:
        print("Contact can't found")
def delete():
    name = input("Enter contact name to delete:")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("Contact can't found.")
def main():
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Enter your choice: ")
        if choice=='1':
            add()
        elif choice=='2':
            view()
        elif choice=='3':
            search()
        elif choice=='4':
            update()
        elif choice=='5':
            delete()
        elif choice=='6':
            print("Exit program")
            break
        else:
            print("Invalid choice.")
main()
