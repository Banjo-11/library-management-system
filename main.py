
from book_manager import add_book, view_books, search_book, remove_book

while True:
    print("\nLIBRARY MANAGEMENT SYSTEM")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Remove a book")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        print(add_book(title))

    elif choice == "2":
        books = view_books()

        if len(books) == 0:
            print("No books available.")
        else:
            print("\nBooks in the library:")
            for book in books:
                print("-", book)

    elif choice == "3":
        title = input("Enter book title to search: ")
        result = search_book(title)

        if result:
            print("Book found:", result)
        else:
            print("Book not found.")

    elif choice == "4":
        title = input("Enter book title to remove: ")
        print(remove_book(title))

    elif choice == "5":
        print("Thank you for using the library system!")
        break

    else:
        print("Invalid option. Please try again.")
