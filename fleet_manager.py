def main():
    n = ["Picard", "Riker", "Data", "Worf", "Spork"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    d = ["Command", "Command", "Operations", "Security", "Science"]
    id=[1, 2, 3, 4, 5]
    list=[n, r, d, id]


    def display_menu():
        name=input("What is your Full Name: ")
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
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
                    n.append(b)
                    r.append(c)
                    d.append(e)
                    id.append(a)
                    print(f"{n} {r} {d} {id}")
        add_member()

        def remove_member():
            if opt=="3":
                g=int(input("Which ID would you like removed: "))
                h=g-1
                id.remove(g)
                del n[h]
                del r[h]
                del d[h]    
                print(f"{n} {r} {d} {id}")
        remove_member()
    display_menu()

main()