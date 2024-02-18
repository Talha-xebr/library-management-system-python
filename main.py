from core.library import Library, Book
import helpers.inputcheckers as inpChecker



def main():
    lib = Library()

    # MENU 
    while True:
        print("\n*** MENU ***\n1)List Books\n2)Add Book\n3)Remove Book\nq)Quit\n")
        menu_selection = input("Select : ").strip().lower()
        
        # QUIT 
        if(menu_selection == 'q'):
            print("Closing Program....")
            break;
    
        # LIST
        elif(menu_selection == '1'):
            lib.listBooks()
            
        
        # ADD
        elif(menu_selection == '2'):
            lib.addBook()
        
        # REMOVE
        elif(menu_selection == '3'):
            lib.removeBook()

        else:
            print("Input is wrong...\nSelect 1 2 3 or q for quit\n-------------")

if __name__== "__main__":
    main()