# Online Library Management System
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

class Libraray:
    
    def __init__(self, listofbook, libname):
        self.listofbook=listofbook
        self.libname=libname
        self.landdict={}
        
    def dispbooklist(self):
        print(f"We have following books in our library :Gunjan singh Library........")
        for book in self.listofbook:
            print(book)
        
    def lendbook(self, name, book):
        if book not in self.landdict.keys():
            self.landdict.update({book:name})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"this book is alreday taken by: {self.landdict(book)}")
        

    def addbooklist(self, book):
        self.listofbook.append(book)
        print("book has been updated succesfully ")

    def returnbook(self, book):
        self.landdict.pop(book)
                
if __name__ == '__main__':
    mylib=Libraray(["RAMAYANA", "GEETA", "ENGLISH", "LEARN PYTHON", "CHEMISTRY", "JUMBA CLASSES"], "gunjanlibrary" )


    while(True):
        print(f"welcome to Gunjan Library . enter your choice to continue")
        print("1. display the books")
        print("2. Land a book")
        print("3. add a book")
        print("4. return a book")

        user_choice=int(input("Enter your Choice : "))
        if user_choice==1:
            mylib.dispbooklist()
        
        elif user_choice==2:
            book=input("Enter the book name which you want to land : ")
            name=input("enter your name :")
            mylib.lendbook(name, book)
            
        elif user_choice==3:
            book=input("Enter the book name which you want to add :")
            mylib.addbooklist(book)
        elif user_choice==4:
            book=input("Enter the book name which you want to return :")
            mylib.returnbook(book)
        else:
            print("you press not a valid option")

        print("press q for quit and c for continue")
        user_choice2=input()
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input("press your choice here :")
            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue

    
    

    


