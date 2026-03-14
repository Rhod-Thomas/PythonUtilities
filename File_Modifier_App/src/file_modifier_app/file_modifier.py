
#Python class that allows for opening a file in binary format and overwriting 
#at the target index with the bytes provided.  

class file_modifier:
    
    def __init__(self):
        self.file = None
        
    def open_file(self, filename):
        self.file = open(filename, "+")
        
        
    def change_file(self, index, bytes_to_write):
        
        if not self.file :
            return (False, "No file loaded!")
        
        try:
            
            self.file.seek(index, 0)
            self.file.write(bytes_to_write)
            return (True, "File modified!")
        
        except Exception as ex:
            return (False, f"Exception: {ex}")
    
    #def read_all_file(self):
        
        