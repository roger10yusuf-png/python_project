library_records = {}

while True:
    print("Library Management System")
    print("1. Borrow a Book")
    print("2. Retrieve Customer Information")
    print("3. Return a Book")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter customer name: ")
        book = input("Enter book name: ")
        author = input("Enter author name: ")
        period = int(input("Enter period of borrow (in days): "))
        library_records[name] = [book, author, period]
        print(f"\nBook '{book}' by {author} borrowed by {name} for {period} days.")

    elif choice == "2":
        name = input("Enter customer name to retrieve details: ")
        if name in library_records:
            info = library_records[name]
            print(f"\nCustomer: {name}")
            print(f"Book: {info[0]}")
            print(f"Author: {info[1]}")
            print(f"Borrow Period: {info[2]} days")
        else:
            print("No record found for this customer.")

    elif choice == "3":
        name = input("Enter customer name returning the book: ")
        if name in library_records:
            actual_days = int(input("Enter actual number of days the book was kept: "))
            borrowed_period = library_records[name][2]
            if actual_days > borrowed_period:
                print("Book returned late. Fine = $500")
            else:
                print("Thank you for returning the book on time!")
            del library_records[name]
        else:
            print("No record found for this customer.")

    elif choice == "4":
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
