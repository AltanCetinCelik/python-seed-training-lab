while True:

    print("=== Seed Control Room v0 ===")
    print("1. Show SEED status")
    print("2. Machine Health check")
    print("3. Add journal line")
    print("4. Show Training goal")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == "1":
        print("You chose 1...Checking SEED status...")
        print("Seed status: foundation stage")
        print("Memory: not persistent yet")
        print("Reflection: manual only")
        print("Tools: locked")
        print("Autonomy: disabled")
    elif choice == "2":
        warning_found=False
        machine_temp = int(input("Temperature: ")) 
        machine_vibe=int(input("Vibration: "))
        machine_mA=int(input("Current mA: "))
        machine_status=input("Motor state: ")
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
        print(f"Machine temp: {machine_temp}°C, \nVibration: {machine_vibe}mm/s, \nCurrent: {machine_mA}mA, \nStatus: {machine_status}")
        print(f"Status check: {machine_temp_war}, \n{machine_vibe_war}, \n{machine_mA_war}, \n{machine_status_war}")
    elif choice == "3":
        journal_entry = input("What happened today?")
        print(f"Journal recieved: {journal_entry} \n Note: persistent memory comes later")
    elif choice == "4":
        print("Checking today's goal...")
        print("Prove I can control python basics by writing an interactive terminal program")
    elif choice == "5":
        print("closing")
        break
    else:
        print("Invalid choice, please try again.")

