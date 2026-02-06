def main(): #Mistake 1: Not including def main() and main()
    n = ["Picard", "Riker", "Data", "Worf"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant"]
    d = ["Command", "Command", "Operations", "Security"]

    active = True

    def run_system_monolith():
        print("BOOTING SYSTEM...")
        print("...")
        print("WELCOME TO FLEET COMMAND")
    run_system_monolith() #Mistake 2: did not properly define function, forgot this part.
    
    def loading(): #Mistake 3: Did not Define Loading  
        loading = 0
        while loading < 5:
            print("Loading module " + str(loading))
            break #Mistake 4: Forgot to insert Break
        
        while True:
            print("\n--- MENU ---")
            print("1. View Crew")
            print("2. Add Crew")
            print("3. Remove Crew")
            print("4. Analyze Data")
            print("5. Exit")
        
            opt = input("Select option: ")
        
            if opt == "1":  #Mistake 5: Only put 1 equal sign not 2
                print("Current Crew List:")
            
                for i in range(10):
                    print(n[i] + " - " + r[i]) 
                    break #Mistake 6: Forgot to put break
                break #Mistake 6: Forgot to put break
                
            elif opt == "2":
                new_name = input("Name: ")
                new_rank = input("Rank: ")
                new_div = input("Division: ")
            
                n.append(new_name)
                print("Crew member added.")
                break #Mistake 7: Forgot to add break

            elif opt == "3":
                rem = input("Name to remove: ")
           
                idx = n.index(rem)
                n.pop(idx)
                r.pop(idx)
                d.pop(idx)
                print("Removed.")
                break #Mistake 8: Forgot to add Break
            
            elif opt == "4":
                print("Analyzing...")
                count = 0
            
                for rank in r:
                    if rank == "Captain" or "Commander": 
                        count = count + 1
                print("High ranking officers: " + str(count)) #Mistake 9: Forgot to type cast it as string
                break #Mistake 10: Forgot to add Break
            elif opt == "5":
                print("Shutting down.")
                break
            
            else:
                print("Invalid.")
            
        
        x = 10 #Mistake 11: Indentation Issue
        if x > 5:
            print("System Check OK")
        else:
            print("System Failure")
            
       
        if len(n) > 0:
            print("Database has entries.")
        if len(n) == 0:
            print("Database empty.")

        
        fuel = 100
        consumption = 0
        while fuel > 0:
            
            print("Idling...")
            break 
            
        print("End of cycle.")

main()