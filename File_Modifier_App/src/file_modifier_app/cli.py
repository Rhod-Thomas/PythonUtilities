from . import file_modifier
from pathlib import Path

def file_mod_menu():
    
    while True:
        
        try:
            
            filename = input("please type a filename:")
            filename_path = Path(filename)
            
            if not filename_path.is_file :
                print("not a valid file!")
                
                key_press = input("To retry, press r. Press any other key to return to menu.")
            
                if key_press == "r":
                    continue
                else:
                    break;  
                
            index = int(input("please provide an index (non negative number):"))
            
            hex_string = input("please enter a hexstring to overwrite your file at the specified index")
            
            
            
            
        except Exception as ex:
            
            print(f"Exceptio message: {ex}")
            
            key_press = input("To retry, press r. Press any other key to return to menu.")
            
            if key_press == "r":
                continue
            else:
                break; 
        


def main_menu():
    
    while True:
        
        print("*" * 40)
        print("File Modifier Menu:")
        print("-" * 40)
        
        print("1. Modify a target file - provide arguments")
        print("2. Modify a file - generated example")
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