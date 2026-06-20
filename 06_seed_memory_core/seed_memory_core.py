import json

MEMORY_FILE = "memories.json"


def load_memories():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Memory file not found. Starting with empty memory.")
        return []

    except json.JSONDecodeError:
        print("Memory file is empty or broken. Starting with empty memory.")
        return []


def save_memories():
    with open(MEMORY_FILE, "w") as file:
        json.dump(memories, file, indent=4)


memories = load_memories()


def menu():
    print("\n=== SEED MEMORY CORE v0 ===")
    print("1. Add memory")
    print("2. List memories")
    print("3. Search memory by type")
    print("4. Delete memory by number")
    print("5. Exit")

    choice = input("Enter your choice: ")
    return choice


def add_memory():
    memory_type = input("Memory type: ")
    content = input("Content: ")

    if content == "":
        print("Memory content cannot be empty.")
        return

    try:
        importance = int(input("Importance (1-5): "))
    except ValueError:
        print("Invalid importance. Please enter a number between 1 and 5.")
        return

    if importance < 1 or importance > 5:
        print("Importance must be between 1 and 5.")
        return

    memory = {
        "type": memory_type,
        "content": content,
        "importance": importance
    }

    memories.append(memory)
    save_memories()

    print("Memory added.")


def list_memories():
    if not memories:
        print("No memories found.")
        return

    print("\n=== MEMORIES ===")

    for number, memory in enumerate(memories, start=1):
        print(
            f"{number}. "
            f"[{memory['type']}] "
            f"{memory['content']} "
            f"Importance: {memory['importance']}"
        )


def search_memory():
    if not memories:
        print("No memories found.")
        return

    search_type = input("Enter memory type to search: ")

    found_memories = []

    for memory in memories:
        if memory["type"] == search_type:
            found_memories.append(memory)

    if not found_memories:
        print("No matching memories found.")
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

    try:
        delete_number = int(input("Enter the number of the memory to delete: "))
    except ValueError:
        print("Invalid number. Please enter a valid memory number.")
        return

    delete_index = delete_number - 1

    if delete_index < 0 or delete_index >= len(memories):
        print("Invalid memory number.")
        return

    confirm = input("Type DELETE to confirm: ")

    if confirm == "DELETE":
        deleted_memory = memories.pop(delete_index)
        save_memories()
        print(f"Deleted memory: {deleted_memory['content']}")
    else:
        print("Delete cancelled.")


def main():
    while True:
        choice = menu()

        if choice == "1":
            add_memory()

        elif choice == "2":
            list_memories()

        elif choice == "3":
            search_memory()

        elif choice == "4":
            delete_memory()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


main()