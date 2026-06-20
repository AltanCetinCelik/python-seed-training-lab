def menu():
    print("1. Add journal entry")
    print("2. Read journal")
    print("3. Clear journal")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice
def file_write():
    with open("journal.txt", "a") as file:
        file.write(input("Enter your journal entry: ") + "\n")
        print("Journal entry added.")
def file_read():
    with open("journal.txt", "r") as file:
        print("Journal entries: ")
        content = file.read()
        if content == "":
            print("No journal entries found.")
        else:
            print(content)
def file_clear():
    delete = input("Are you sure you want to clear the journal? (y/n): ")
    if delete == "y":
        with open("journal.txt", "w") as file:
            file.write("")
            print("Journal cleared.")
    else:
        print("Journal not cleared.")
def main():
    while True:
        choice = menu()
        if choice == "1":
            file_write()
        elif choice == "2":
            file_read()
        elif choice == "3":
            file_clear()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()



