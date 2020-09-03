class Library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lendDict={}
    def displaybooks(self):
        print("We have the following books")
        for book in self.bookslist:
            print(book)
    def lendbooks(self,user,book):
        if book  not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Book Dictionary has been updated")
        else:
            print("Book is already being taken by someone")


    def addbooks(self,book):
        self.bookslist.append(book)
        print("Book has been added to Booklist")
    def returnbooks(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
        akshat=Library(["The God of Small Things","Lowland","War and Peace","Sherlock Holmes","Dracula",],"Astra Universe")
        while(True):
            print("Welcome to the Akshat's library.\nEnter your choice to continue.")
            print("1.Display a Book")
            print("2.Lend a Book")
            print("3.Add a Book")
            print("4.Return a Book")
            user_choice=input()
            if user_choice not in ["1","2","3","4"]:
                continue
            else:
                user_choice=int(user_choice)
            if user_choice==1:
                akshat.displaybooks()
            elif user_choice==2:
                book=input("Enter your Book to lend")
                user=input("Enter your name")
                akshat.lendbooks(user,book)
            elif user_choice==3:
                book = input("Enter your Book to add")
                akshat.addbooks(book)
            elif user_choice==4:
                book = input("Enter your Book to return")
                akshat.returnbooks(book)
            else:
                print("Not a valid option")
            print("Press q to quit or c to continue")
            user_choice2=""
            while(user_choice2!="q" and user_choice2!="c"):
                user_choice2=input()
                if user_choice2=="q":
                    exit()
                if user_choice2=="c":
                    continue

