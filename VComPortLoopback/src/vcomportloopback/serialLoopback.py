##Com port loopback test file. 
from exceptiongroup import catch
import serial

#globals/cached 
lastPort = ""
lastBaud = 0

def configureComPort(COM, Baud, Timeout = 1, RTSCTS = False):
    
    try :
        with serial.Serial(COM, Baud, timeout=Timeout, rtscts=RTSCTS) as ser:
            ser.write(b'Hello from the world of tomorrow!')
            
            #cache those working parameters:
            global lastPort
            lastPort= COM
            global lastBaud
            lastBaud= Baud
            
            return True
               
    except Exception as ex:
        return False
    


def simpleLoopback():
    
    try:
        with serial.Serial(lastPort, lastBaud, timeout=1) as ser:
            
            sendMessage = b'hello loopback!'
            ser.write(sendMessage)
            
            receiveMessage = ser.read(len(sendMessage))
            
            if(receiveMessage == sendMessage):
                return True
                 
            else:
                return False
        
    except Exception as e:
        print(f"Error: {e}")        
    
   
##Check that config is populated before returning  
def getConfig():
    
    [com, baud] = "", 0
    
    if not lastPort or baud == 0:
        return ["", 0]
    
    return [lastPort, lastBaud]