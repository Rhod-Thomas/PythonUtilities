import pathlib

#Python class that allows for opening a file in binary format and overwriting 
#at the target index with the bytes provided.  

class file_modifier:
    
    ###
    def __init__(self):
        self.file = None    
        
    ###    
    def open_file(self, filename):
        
        try:
            
            self.file = open(filename, "rb+")
            return(True, "File opened for writing.")
            
        except Exception as ex:
            
            return(False, "File NOT opened.")    
        
    ###            
    def change_file(self, index, bytes_to_write):
        
        if not self.file :
            
            return (False, "No file opened.")
        
        try:
            
            self.file.seek(index, 0)
            self.file.write(bytes_to_write)
            return (True, "File modified!")
        
        except Exception as ex:
            return (False, f"Exception: {ex}")

            
def main():
    
    ##TODO; this would be better done using PyTest - port someday. 
    
    ##setup
    ##Create a completely clean file with 
     
    target_path = '../output/file_modifier_test.bin'
    
    path = pathlib.Path(target_path)
    path.unlink(missing_ok=True) 
    
    ##create a file with 20 bytes of FF.  
    with open(target_path, "wb+") as file:        
        file.write(b'\xFF' * 20)
    
    #entry point for testing the class 
    testfile = file_modifier()
    success, message = testfile.open_file('../output/file_modifier_test.bin')
     
    print(message)
     
    if success == True :
        
        index = 8
        data = b'\x00\x00'
        print(f"putting data: {data}, at index: {index}")
        success, message = testfile.change_file(index, data)
        print(message)         

                  
if __name__ == "__main__":
       main()
        