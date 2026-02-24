from tracker import LanguageTracker

my_robot = LanguageTracker("study_log.txt")

def show_menu():
    print("\n--- 📍 Smart Language Hub ---")
    print("1: Save New")
    print("2: Open Save")
    print("3: Clear Log")
    print("0: Exit")
    return  input("Select an option: ")

while True:
    choice = show_menu()

    if choice == "1":
        lang = input("Select language: ")
        detail = input("Select detail: ")
        my_robot.add_task(lang, detail)
    elif choice == "2":
        my_robot.view_tasks()
    elif choice == "3":
        confirm = input("Do you want to save the data? (y/n): ")
        if confirm.lower() == "y":
            my_robot.delete_all()
    elif choice == "0":
        print("Thank you for using Smart Language Hub")
        break
    else:
        print("Invalid option")

