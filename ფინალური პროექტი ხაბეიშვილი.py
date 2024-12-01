
# წიგნის კლასის შექმნა შესაბამისი ატრიბუტებით
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class BookManager:
    def __init__(self):
        self.books = []

        # წინასწარ დამატებული წიგნები სატესტოდ
        self.books.append(Book("lotr", "J.R.R. Tolkien", 1954))
        self.books.append(Book("got", "George R.R. Martin", 1996))

    # წიგნების დამატება და დუბლირების შემოწმება
    def add_book(self, title, author, year):
        if any(book.title.lower() == title.lower() for book in self.books):
            print(" This book already exists in the list. Here are its details:")
            for book in self.books:
                if book.title.lower() == title.lower():
                    print(book)
            return

        book = Book(title, author, year)
        self.books.append(book)
        print(" Book has been added to the list!")

    # წიგნების სრული სიის ნახვა
    def list_books(self):
        if not self.books:
            print(" The book list is empty. Add some books!")
        else:
            print(" All the books in the list:")
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    # წიგნის ძებნა სახელის მიხედვით
    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if not found_books:
            print(f" Book '{title}' can't be found.")
        else:
            print(" Found books:")
            for book in found_books:
                print(book)


class UserInterface:
    def __init__(self):
        self.manager = BookManager()

    def run(self):
        while True:
            print("\n Book Management System")
            print("1. Add new book")
            print("2. See all books")
            print("3. Search by name")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                title = input("Please input the book name: ").strip()
                author = input("Please input the author: ").strip()

                # ცარიელი შეყვანის ვალიდაცია
                if not title or not author:
                    print(" Title and Author cannot be empty!")
                    continue
                #ვალიდაცია სწორი მონაცემის ტიპის შეყვანისთვის
                try:
                    year = int(input("Please input the publish year: ").strip())
                except ValueError:
                    print(" Please enter a valid year!")
                    continue

                self.manager.add_book(title, author, year)

            elif choice == "2":
                self.manager.list_books()

            elif choice == "3":
                title = input("Please enter book name for search: ").strip()
                if not title:
                    print(" Search term cannot be empty!")
                    continue
                self.manager.search_book(title)

            elif choice == "4":
                print(" Goodbye! Have a great day!")
                break

            else:
                print(" Incorrect input. Please enter a number from 1 to 4.")


# პროგრამის გაშვება
ui = UserInterface()
ui.run()