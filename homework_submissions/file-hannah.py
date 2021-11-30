def adding():

    file = open("list", 'a')
    user_input = input("Enter the item you want to add: ")
    file.writelines(f"{user_input}\n")
    file.close()
    print("\nSuccessfully added to the list")


def viewing():

    file = open("list", 'r')
    r = file.read()
    print(f"\n{r}")


def delete():

    input_ = input("Enter the item you want to delete: ")
    file = open("list", 'r')
    lst = file.readlines()
    new_file = open("list", 'w')

    for item in lst:
        if item != f"{input_}\n":
            new_file.writelines(item)

    print("\nSuccessfully deleted from the list")


def what_to_do():

    input_ = input("Enter 'a' to add an item; Enter 'd' to delete and item; Enter 'v' to view the list\n")

    if input_ == "a":
        print(adding())
    elif input_ == "d":
        print(delete())
    elif input_.lower() == "v":
        print(viewing())


what_to_do()