
def show_menu():
    print("=== Seed Control Room v0 ===")
    print("1. Show SEED status")
    print("2. Machine Health check")
    print("3. Add journal line")
    print("4. Show Training goal")
    print("5. Exit")
   
   
def show_seed_status():
    print("You chose 1...Checking SEED status...")
    print("Seed status: foundation stage")
    print("Memory: not persistent yet")
    print("Reflection: manual only")
    print("Tools: locked")
    print("Autonomy: disabled")
    
def machine_health_check():
    warning_found = False
    machine_temp = int(input("Temperature: ")) 
    machine_vibe = int(input("Vibration: "))
    machine_mA = int(input("Current mA: "))
    motor_state = input("Motor state: ")
    machine_status_war = "machine status normal"
    machine_temp_war = "temperature normal"
    machine_vibe_war = "vibration normal"
    machine_mA_war = "current normal"
    if machine_temp > 40:
        machine_temp_war = "warning"
        warning_found=True
    if machine_vibe > 60:
        machine_vibe_war = "warning"
        warning_found=True
    if machine_mA > 300:
        machine_mA_war = "warning"
        warning_found=True
    if warning_found:
        machine_status_war = "machine status warning"
    else:
        machine_status_war = "machine status normal"  
    print(f"Machine temp: {machine_temp}°C, \nVibration: {machine_vibe}mm/s, \nCurrent: {machine_mA}mA, \nStatus: {motor_state}")
    print(f"Status check: {machine_temp_war}, \n{machine_vibe_war}, \n{machine_mA_war}, \n{machine_status_war}")

def add_journal_line():
    journal_entry = input("What happened today?")
    print(f"Journal recieved: {journal_entry} \n Note: persistent memory comes later")
    
def show_training_goal():
    print("Checking today's goal...")
    print("Prove I can control python basics by writing an interactive terminal program")
def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            show_seed_status()
        elif choice == "2":
            machine_health_check()
        elif choice == "3":
            add_journal_line()
        elif choice == "4":
            show_training_goal()
        elif choice == "5":
            print("closing")
            break
        else:
            print("Invalid choice, please try again.")
main()
