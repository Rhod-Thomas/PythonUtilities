import serial 

class SerialPort:
    def __init__(self):
        self.ser = None
        
    def open_port(self, COM, baud_rate):
        
        try:    
            self.ser = serial.Serial(COM, baud_rate)
            return (True, "Successfully opened Com Port") 
            
        except Exception as ex:
            return (False, f"Failed because: {ex}")
    
    def open_port_menu(self):
        print("Menu")
        
        
    def send_data(self, data_to_send):
        print("Sending data")
        
        if not self.ser or not self.ser.is_open(): 
            return (False, "Com port not open/configured")
            
        
    def receive_data(self, data_to_send):
        print("Sending data")
        
        if not self.ser or not self.ser.is_open(): 
            return (False, "Com port not open/configured")
        
          
    def send_receive_data(self, data_to_send, expected_response):
        print("Sending data then waiting for response")
        
        if not self.ser or not self.ser.is_open(): 
            return (False, "Com port not open/configured")
        
        