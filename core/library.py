from core.book import Book
from prettytable import PrettyTable
import helpers.inputcheckers as inpChecker

# 1. Create Class Library
class Library:
    # 1.a : Constructor
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")
        self.fileString = self.getFileString()
        self.book_list = []

        

    # 1.a. : Destructor
    def __del__(self):
        self.file.close()


    def getFileString(self):
        self.file.seek(0)
        return self.file.read()

    def updateBookList(self):
        if not self.fileString:
           self.fileString = self.getFileString()
        
        self.book_list.clear()

        for line in self.fileString.splitlines():
            self.book_list.append(line.split(","))
    
    # 2.a : List books
    def listBooks(self):
        if not self.fileString:
            self.fileString = self.getFileString()
        
        bookList = self.fileString.splitlines()
        if not bookList:
            print("\nNo books found in the library.")
        else:
            pTable = PrettyTable()
            pTable.field_names = ["Title","Author","Release Year","Number of Pages"]
            
            for line in bookList:
                title, author, year, pages = line.split(",")
                pTable.add_row([title,author,year,pages])

            print(pTable)

    # 2.b : Add Book
    def addBook(self):
        
        # TODO : ASK FOR ADD ANOTHER BOOK INPUT

        while True:


            title = inpChecker.checkEmptyStr("Book Title : ")
            author = inpChecker.checkEmptyStr("Book Author : ")
            release_year = str(inpChecker.checkPositiveIntInput("Release Year : "))
            pages = str(inpChecker.checkPositiveIntInput("Number of Pages : "))

            #book = ",".join([title, author, release_year, pages])
            bookObj = Book(title=title, author=author,release_year=release_year,number_of_pages=pages)
            book = bookObj.toString() 

            if self.fileString:
                # file is not empty
                # get last line
                last_line = self.fileString.splitlines()[-1]
                if not (self.fileString[-1] == "\n"):
                    # this means last line not created a new line
                    # is this line empty
                    if (len(last_line.strip())==0) and (len(last_line) >=1):
                        # contains spaces
                        # if this line is empty and not created a new line, write and add line
                        self.file.write(book+"\n")
                    elif (len(last_line.strip())==0) and (len(last_line) == 0):
                        # its just empty, not contains spaces, but empty
                        self.file.write(book+"\n")       
                    else:
                        # line is not empty, add line and write
                        self.file.write("\n"+book)
                else:
                    # new line write and go
                    self.file.write(book+"\n")     
            else:
                # file is empty, write and create a line
                self.file.write(book+"\n")
            
            self.file.flush()
            self.fileString = self.getFileString()
            self.updateBookList()

            
            print("\Add another book? \nPress 'y' for confirm, Press anything for menu.\n")
            add_choice = inpChecker.checkEmptyStr("Choice :")
            
            if (add_choice.strip().lower() != "y"):
                break


        
    # 2.c : remove book
    def removeBook(self):
        if not self.fileString:
            self.fileString = self.getFileString() 
        if not self.book_list:
            self.updateBookList()
        try:
            deletion_title = inpChecker.checkEmptyStr("Write the Title of the Book you want to delete : ")
            # 2.c.iii Find the index of the book to be deleted
            deletion_index = -1
            for book in self.book_list:  
                if(book[0] == deletion_title):
                    deletion_index = self.book_list.index(book)
                    break
            
            if deletion_index >= 0: 
                print("\nDeleting This Book : ", self.book_list[deletion_index])
                
                confirmation = (input("\nAre you sure? Y/N : ")).lower()
                
                if(confirmation == "y"):
                    # 2.c.iv : remove the book
                    self.book_list.pop(deletion_index)
                
                    # 2.c.v : remove contents from .txt
                    self.file.seek(0)
                    self.file.truncate()
                
                    # 2.c.vi : add all elements of the list to txt
                    updatedString = "\n".join([",".join(map(str, book)) for book in self.book_list])
                
                    self.file.write(updatedString) 
                    self.file.flush()
                    
                    self.fileString = updatedString
                    self.updateBookList()
                    
                    print("\nBook Deleted and File Updated Successfully")

                else:
                    print("\nDeletion cancelled...")
            else:
                print("\nBook not found...")
       
        except Exception as err:
            print(f"An Error Occured While Deleting...\n{err}")
