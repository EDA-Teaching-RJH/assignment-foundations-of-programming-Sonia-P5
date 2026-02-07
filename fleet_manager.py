def main():
    Names = ["Picard", "Riker", "Data", "Worf", "Spork"]
    Ranks = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    Divisions = ["Command", "Command", "Operations", "Security", "Science"]
    IDs=[1, 2, 3, 4, 5]
    list=[Names, Ranks, Divisions, IDs]


    def display_menu():
        name=input("What is your Full Name: ")
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Update Rank")
        print("5. Display Roster")
        print("6. Search for a Crew")
        print("7. Filter")
        print("8. Credit Assigned to Each Rank")
        print("9. # of Captains or Commanders")
        print(f"Current Student Logged in: {name}")
        opt = input("Select option: ")

        def init_database():
            if opt=="1":
                print(list)
        init_database()

        def add_member():
            if opt=="2":
                a=int(input("Enter a new ID: "))
                while a<=5:
                    print("ID already exists")
                    a=int(input("Enter a new ID: "))
                    
                else:
                    b=input("Enter Name: ")
                    c=input("Enter Rank: ")
                    e=input("Enter Division: ")

                    while c!="Captain" or c!="Commander" or c!="Lt. Commander" or c!="Lieutenant":
                        print("Invalid")
                        c=input("Enter Rank: ")
                        break
                    Names.append(b)
                    Ranks.append(c)
                    Divisions.append(e)
                    IDs.append(a)
                    print(f"{Names} {Ranks} {Divisions} {IDs}")
        add_member()

        def remove_member():
            if opt=="3":
                g=int(input("Which ID would you like removed: "))
                h=g-1
                IDs.remove(g)
                del Names[h]
                del Ranks[h]
                del Divisions[h]    
                print(f"{Names} {Ranks} {Divisions} {IDs}")
        remove_member()

        def update_rank():
            if opt=="4":
                j=int(input("Enter the ID of the member you would like to update: "))
                l=j-1
                m=str(input("What would you like to update them to: "))
                Ranks[l]=m
                print(f"{Names} {Ranks} {Divisions} {IDs}")
        update_rank()

        def display_roster():
            if opt=="5":
                print("----TABLE----")
                print("NAMES")
                for x in range(len(Names)):
                    print(f"{x+1} {Names[x]}")
                
                print("RANK")
                for x in range(len(Ranks)):
                    print(f"{x+1} {Ranks[x]}")

                print("DIVISION")
                for x in range(len(Divisions)):
                    print(f"{x+1} {Divisions[x]}")

                print("ID")
                for x in range(len(Names)):
                    print(f"{x+1} {IDs[x]}")
        display_roster()

        def search_crew():
            if opt=="6":
                o=str(input("Input a Search Term: "))
                if o=='Captain':
                    print("Result: Picard and Spock")
                elif o=="Commander":
                    print("Result: Riker")
                elif o=="Lt. Commander":    
                    print("Result: Data")
                elif o=="Lieutenant":
                    print("Result: Worf")
                else:
                    print("Invalid Input")
        search_crew()

        def filter_by_division():
            if opt=="7":
                p=input("Select one of the following: Command, Operations, Security, or Sciences: ")

                if p=="Command":
                    print("Picard and Riker")
                elif p=="Operations": 
                    print("Data")
                elif p=="Security":
                    print("Worf")
                elif p=="Sciences":
                    print("Spock")
                else:
                    print("Invalid Input")
                    p=input("Select one of the following: Command, Operations, Security, or Sciences")  
        filter_by_division()

        def calculate_payroll():
            if opt=="8":
                credit=[1000, 3000, 500, 30, 1000]
                for x in range(len(Names)):
                    print(f"{x+1} {Names[x]} {credit[x]}")
        calculate_payroll()

        def count_officers():
            if opt=="9":
                q=input("Select one of the following to discover how many people are in said rank position (Captain or Commander): ")
                if q=="Captain":
                    print("2")
                elif q=="Commander":
                    print("1")
                else:
                    print("Invalid Input")
                    q=input("Select one of the following to discover how many people are in said rank position (Captain or Commander): ")      
        count_officers()

        

    display_menu()

main()