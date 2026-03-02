##Com port loopback test file. 

from exceptiongroup import catch
import serial

#globals/cached 
lastPort = ""
lastBaud = 0

def test_loopback():
    
    target = input("Enter the target COM port path and baud rate(e.g., COM3 9600).")
    
    try:
        port, baud = target.split()
        
        with serial.Serial(port, int(baud), timeout=1) as ser:
            
            sendMessage = b'hello loopback!'
            ser.write(sendMessage)
            
            receiveMessage = ser.read(len(sendMessage))
            
            if(receiveMessage == sendMessage):
                print("Loopback worked!!")
                print("Caching Port and baud.")
                
                global lastPort
                global lastBaud
                
                lastPort = port
                lastBaud = baud
                 
            else:
                print("Error: No loopback of message.") 
        
    except Exception as e:
        print(f"Error: {e}")
    
def test_others():
    print("Test others function executed")

def main_menu():
    
    while True:
        
        print("*" * 40)
        print("Main Menu:")
        print("*" * 40)
        
        print("1. Test Loopback")
        print("2. Test Others")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            test_loopback()
        elif choice == '2':
            test_others()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")    
            
        input("Press Enter to continue...")
        
        print("")
        print("")
        