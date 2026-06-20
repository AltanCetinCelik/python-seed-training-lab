import json
def save_memories():
    with open("memories.json", "w") as f:
        json.dump(memories, f, indent=4)
def load_memories():
    with open("memories.json", "r") as f:
        return json.load(f)
memories = load_memories()    
def menu():
    print("1. Add memory")
    print("2. List memories")
    print("3. Search memory by type")
    print("4. Delete memory by type")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice
def add_memory():
    memory = {
        "type": input("Memory type:" ),
        "content": input("Content: "),
        "importance": int(input("Importance (1-5): "))
    }
    memories.append(memory)
    print("Memory added.")

def list_memories():
    if not memories:
        print("No memories found.")
        return
    else:
        print("Memories: ")
        for number,memory in enumerate(memories, start=1):
            print(f"Type: {memory['type']}, Content: {memory['content']}, Importance: {memory['importance']}")


def search_memory():
    search_type = input("Enter memory type to search: ")
    found_memories = []
    for memory in memories:
        if memory['type'] == search_type:
            found_memories.append(memory)
    if not found_memories:
        print("No memories found.")
        return
    print("\n=== SEARCH RESULTS ===")

    for number, memory in enumerate(found_memories, start=1):
        print(
            f"{number}. "
            f"[{memory['type']}] "
            f"{memory['content']} "
            f"Importance: {memory['importance']}"
        )


def delete_memory():
    if not memories:
        print("No memories to delete.")
        return

    list_memories()

    delete_number = int(input("Enter the number of the memory to delete: "))
    delete_index = delete_number - 1

    if delete_index < 0 or delete_index >= len(memories):
        print("Invalid number.")
        return

    confirm = input("Type DELETE to confirm: ")

    if confirm == "DELETE":
        deleted_memory = memories.pop(delete_index)
        print(f"Deleted memory: {deleted_memory['content']}")
    else:
        print("Delete cancelled.")


def main():
    while True:
        choice = menu()

        if choice == "1":
            add_memory()
            save_memories()

        elif choice == "2":
            list_memories()

        elif choice == "3":
            search_memory()

        elif choice == "4":
            delete_memory()
            save_memories()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


main()



        




