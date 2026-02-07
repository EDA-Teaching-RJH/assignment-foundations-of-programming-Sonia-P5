def main():
    n = ["Picard", "Riker", "Data", "Worf", "Spork"]
    r = ["Captain", "Commander", "Lt. Commander", "Lieutenant", "Captain"]
    d = ["Command", "Command", "Operations", "Security", "Science"]
    id=[1, 2, 3, 4, 5]
    list=[n, r, d, id]


    def run_system_monolith():
        print("\n--- MENU ---")
        print("1. View Crew")
        print("2. Add Crew")
        print("3. Remove Crew")
        print("4. Analyze Data")
        print("5. Exit")
        opt = input("Select option: ")

        def init_database():
            if opt=="1":
                print(list)
        init_database()

    run_system_monolith()

main()