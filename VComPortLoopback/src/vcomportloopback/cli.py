from . import serialLoopback

## command line interface for testing serial loopback hardware
def main_menu():
    
    while True:
        
        print("*" * 40)
        print("Main Menu:")
        print("-" * 40)
        
        print("1. Test Loopback")
        print("2. Test Others")
        print("3. Exit")
        print("-" * 40)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            
            target = input("Enter the target COM port and baud rate (default: COM3 9600).")   
            target = target.strip() 
                  
            try:
                port, baud = target.split()
                
                if serialLoopback.configureComPort(port, baud):
                    if serialLoopback.simpleLoopback():
                        print("Successful loopback test!")
                    else:
                        print("Loopback failed")
                else:
                    print("Port config failed")
                        
            except Exception as ex:
                print(ex)
            
        elif choice == '2':
            serialLoopback.test_others()
            
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")    
            
        input("Press Enter to continue...")
        
        print("")