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
        print(f"Current Student Logged in: {name}")
        opt = input("Select option: ")

        def init_database():
            if opt=="1":
                print(list)
        init_database()

        def add_member():
            if opt=="2":
                a=int(input("Insert a New ID: "))

                while a<=5:
                    print("That ID already exists")
                    a=int(input("Enter New ID: "))

                b=str(input("Insert Name: "))
                c=str(input("Insert Rank: "))
                e=(input("Insert Division: "))

                while not c=="Captain" or c=="Commander" or c=="Lt. Commander" or c=="Lieutenant":
                    print("Invalid Rank")
                    c=str(input("Insert Rank: "))

                ids.append(a)
                n.append(b)  
                r.append(c)
                d.append(e)
            print(f"{n} {r} {d} {ids}")
        add_member()
                  
    display_menu()
    
main()