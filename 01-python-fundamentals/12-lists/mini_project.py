'''Library Management System

Store books in a list.

Menu

Add Book

Delete Book

Search Book

Issue Book

Return Book

Display Books

Exit

Use lists only.'''


print('''
  =========Menu==========
        1.Add Book

        2.Delete Book

        3.Search Book

        4.Issue Book

        5.Return Book

        6.Display Books

        7.Exit''')
books = []
issue_book=[]

while True:
    operation = int(input("Enter a number from the menu"))
    if operation == 1:
        book_id = int(input("Enter a book ID"))
        books.append(book_id)
        print(books)
    elif operation == 2:
        book_id = int(input("Enter a book ID"))
        books.remove(book_id)
        print(books)
    elif operation == 3:
        book_id = int(input("Enter a book ID"))
        if book_id in books:
            print('books found')
        else:
            print("Book is not available.")
    elif operation == 4:
        book_id = int(input("Enter a book ID"))
        if book_id in books:
            issue_book.append(book_id)
            books.remove(book_id)
            print("Book issued successfully.")
        else:
            print("Book is not available.")
    elif operation == 5:
        book_id = int(input("Enter a book ID"))
        if book_id in issue_book:
            issue_book.remove(book_id)
            books.append(book_id)
            print(f"{book_id} returned successfully.")
        else:
            print("This book was not issued.")
    elif operation == 6:
        print("Available Books:", books)
        print("Issued Books:", issue_book)
    elif operation == 7:
        print("Thank you!")
        break
    
    
        
    