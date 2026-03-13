
## command line interface template
def main_menu():
    
    while True:
        
        print("*" * 40)
        print("Main Menu:")
        print("-" * 40)
        
        print("1. Choice 1")
        print("2. Choice 2")
        print("3. Choice 3")
        print("4. Exit")
        print("-" * 40)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Selected choice 1")
            
        elif choice == '2':
            print("Selected choice 2")
            
        elif choice == '3':
            print("Selected choice 3")
            
        elif choice == '4':
            print("Exiting!")
            break            
        else:
            print("Invalid choice. Please try again.")    
            
        input("Press Enter to continue...")
        
        print("")