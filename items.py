items = {"dog":"bark","cat":"meow","bird":"chirp"}

while True:
    print("1) View All")
    print("2) Add New")
    print("3) Delete")
    print("4) Change")
    print("5) Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print(items)

    elif choice == "2":
        add_new_key = input("enter: new[key] name:")
        add_new_value = input("enter: new[key] = value name:")
        items [add_new_key] = add_new_value
        print(items)

    elif choice == "3":
        del_ = input("enter:[key] name:")
        del items[del_]
        print(items)

    elif choice == "4":
        change_key = input("enter: the [key] of the value you want to change:")
        change_value = input("enter:[key]s changed value:")
        items [change_key] = change_value
        print(items)   

    elif choice == "5":
        break
    
    else:
        print("Invalid choice.")
