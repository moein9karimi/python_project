class Contact:
    def __init__(self, firstname: str, lastname: str, number: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.number = number

    def __repr__(self) -> str:
        return (
            f"Fullname: {self.firstname} {self.lastname} | Phone number:{self.number}"
        )


class ContactsApp:
    contacts: list[Contact] = []

    def __init__(self, number_of_contacts: int = 0) -> None:
        for i in range(number_of_contacts):
            firstname = input(f"Firstname of contact number {i+1}: ")
            lastname = input(f"Lastname of contact number {i+1}: ")
            number = input(f"Phone number of contact number {i+1}: ")

            print("______________________________________________")
            print("______________________________________________")
            print()
            self.contacts.append(Contact(firstname, lastname, number))

    def __getitem__(self, key: str) -> str:
        for contact in self.contacts:
            if key in (contact.firstname, contact.lastname, contact.number):
                return contact

        print("Contact doesn't exist!")

    def __str__(self) -> str:
        return f"Contacts: {self.contacts}"

    def add(self, contact: Contact) -> None:
        self.contacts.append(contact)

    def delete(self, key: str) -> None:
        for contact in self.contacts:
            if key in (contact.firstname, contact.lastname, contact.number):
                self.contacts.remove(contact)
                return

        print("Contact doesn't exist!")


def main():

    j = int(input("how many contacts do you want to save? "))
    contacts = ContactsApp(j)

    contacts.add

    print(contacts["moein"])
    print("")
    print(contacts["9047"])
    print("")
    print(contacts)


if __name__ == "__main__":
    main()