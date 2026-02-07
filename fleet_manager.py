def main():
    n = ["Picard", "Riker", "Data", "Worf", "Spock"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain" ]
    d = ["Command", "Command", "Operations", "Security", "Science"]
    ids=[1, 2, 3, 4, 5]
    list=[n, r, d, ids]

    print("BOOTING SYSTEM...")
    print("...")
    print("WELCOME TO FLEET COMMAND")

    def display_menu():
        name=input("Insert your Full Name: ")
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Update Rank")
        print("5. Analyze Data")
        print("6. Search Crew")
        print("7. Members of a Division")
        print("8. Credit Value for Each Rank")
        print("9. Count the # of a rank")
        print("10. Exit")
        print(f"Current User Logged in: {name}")
        opt = input("Select option: ")

        def init_database():
            if opt=="1":
                print(list)
        init_database()

        def add_member():
            if opt=="2":
                a=int(input("Insert a new ID: "))
                if a<=5:
                    print("That ID already exists")
                    a=input("Insert a new ID: ")
                else:
                    b=str(input("Insert Name: "))
                    c=str(input("Insert Rank: "))
                    e=(input("Insert Division: "))
                n.append(b)
                r.append(c)
                d.append(e)
                ids.append(a)
                print(f"{n} {r} {d} {ids}")
        add_member()

        def remove_member():
            if opt=="3":
                g=int(input("Which ID would you like removed: "))
                h=g-1
                ids.remove(g)
                del n[h]
                del r[h]
                del d[h]
                
                print(f"{n} {r} {d} {ids}")
                
                
        remove_member()

        def update_rank():
            if opt=="4":
                j=int(input("Enter the ID of the member you would like to update: "))
                l=j-1
                m=str(input("What would you like to update them to: "))
                r[l]=m
                print(f"{n} {r} {d} {ids}")
                        
        update_rank()

        def display_roster():
            if opt=="5":
                print("----TABLE----")
                print("NAMES")
                for x in range(len(n)):
                    print(f"{x+1} {n[x]}")
                
                print("RANK")
                for x in range(len(r)):
                    print(f"{x+1} {r[x]}")

                print("DIVISION")
                for x in range(len(d)):
                    print(f"{x+1} {d[x]}")

                print("ID")
                for x in range(len(ids)):
                    print(f"{x+1} {ids[x]}")
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
                for x in range(len(n)):
                    print(f"{x+1} {n[x]} {credit[x]}")
        
        calculate_payroll()

        def count_officers():
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