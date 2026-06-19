memories = []
def main():
    while True:
        choice = menu()
        if choice == "1":
            add_memory()
        elif choice == "2":
            list_memories()
        elif choice == "3":
            filter_memories()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("1. Add memory")
    print("2. List memories")
    print("3. Filter memories by type")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def add_memory():
    memory_type = input("Memory type: ")
    memory_content = input("Memory content: ")
    importance = int(input("Importance (1-5): "))
    memory = {
        "type": memory_type,
        "content": memory_content,
        "importance": importance
    }
    memories.append(memory)
    print("Memory added. ")
def list_memories():
    print(f"Memories: {memories}")
def filter_memories():
    memory_type = input("Enter memory type to filter: ")
    filtered_memories = [] 
    for memory in memories:
       if memory["type"] == memory_type:
         filtered_memories.append(memory) 
    if not filtered_memories:
        print("No memories found for this type.")
    else:
        print(f"Filtered memories: {filtered_memories}")

main()

