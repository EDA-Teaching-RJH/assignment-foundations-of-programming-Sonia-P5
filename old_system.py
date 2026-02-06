def main(): #Mistake 1: Did not add def main() and main()
    n = ["Picard", "Riker", "Data", "Worf"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    d = ["Command", "Command", "Operations", "Security"]

    active = True

    def run_system_monolith():
        print("BOOTING SYSTEM...")
        print("...")
        print("WELCOME TO FLEET COMMAND")
    run_system_monolith() #Mistake 2: Did not properly defin function, forgot to add this

    loading = 0
    while loading < 5:
        print("Loading module " + str(loading))
        break #Mistake 3: Did not add break

    while True:
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        
        opt = input("Select option: ")

        if opt == "1":  #Mistake 4: Only had one equal sign, two are needed
            print("Current Crew List:")
            
            for i in range(10):
                print(n[i] + " - " + r[i])
                break
            break #Mistake 5: Did not add breaks

        elif opt == "2":
            new_name = input("Name: ")
            new_rank = input("Rank: ")
            new_div = input("Division: ")
            
           
            n.append(new_name)
            print("Crew member added.")
            break #Mistake 6: Did not add break
main()