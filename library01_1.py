class Library:
    def __init__(self, listOfBooks):
       self.books = listOfBooks


    def displayAvalableBooks(self):
            print("The books present in the library are: ")
            for book in self.books:
                print("->" + book)
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.\nThank You! ")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book as been 'issued' to somebody else. Please wait until the book is returned")
            return False


    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the Book.\nHave a great Day!")

     
class Student:
    def requestBook(self):
        self.book = input("Enter the name of the Book you want: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the Book you want to return: ")
        return self.book
       
        

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes", "The Jungle Book", "The Jurasic Park"])
    student = Student()
    # centralLibrary.displayAvalableBooks()
    while(True):
        welcomeMsg =  ''' =====Welcome to 'CENTRAL LIBRARY'=====
        Please choose the option:
        1. List all the books
        2. Request a book
        3. Return a book
        4. Exit the Menu
        '''
        print(welcomeMsg)

        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvalableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing CENTRAL LIBRARY.\nHave a great day!")
            exit()
        else:
            print("Invalid Choice!")
        
