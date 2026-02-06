def main(): #Mistake 1: Did not properly defined function, did not include def main() and main()
    n = ["Picard", "Riker", "Data", "Worf"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    d = ["Command", "Command", "Operations", "Security"]

    active = True

    def run_system_monolith():
        print("BOOTING SYSTEM...")
        print("...")
        print("WELCOME TO FLEET COMMAND")
    run_system_monolith() #Mistake 2: Did not properly define function, forgot to add this
    
    
        loading = 0
        while loading < 5:
            print("Loading module " + str(loading))

main()