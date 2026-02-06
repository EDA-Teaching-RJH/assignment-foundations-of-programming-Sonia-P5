def main(): #Mistake 1: Not including def main() and main()
    n = ["Picard", "Riker", "Data", "Worf"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    d = ["Command", "Command", "Operations", "Security"]

    active=True

    def run_system_monolith():
        print("BOOTING SYSTEM...")
        print("...")
        print("WELCOME TO FLEET COMMAND")
    run_system_monolith() #Mistake 2: Not properly definiing function

    def loading(): #Mistake 3, did not define loading
        loading = 0
        while loading < 5:
            print("Loading module " + str(loading))
            break #Mistake 4, did not add break

        while True:
            print("\n--- MENU ---")
            print("1. View Crew")
            print("2. Add Crew")
            print("3. Remove Crew")
            print("4. Analyze Data")
            print("5. Exit")

            opt = input("Select option: ")

            if opt == "1":  #Mistake 5: Did not put two equal signs
                print("Current Crew List:")
                break
            break #Mistake 6 Break


    
main()