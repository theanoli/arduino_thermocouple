#import serial 
import time

###ISSUES
# Maybe this doesn't need to be a class...?


log = 'temp_log.txt'
open(log,'wb').close()

        
class getTemp():
    def __init__(self):
        self.port = 'COM3'
        self.log = 'temp_log.txt'
        self.tm = None
        
    def checkIfAvailable(self):
        try: 
            self.tm = serial.Serial(self.port, 9600, timeout=None)
            return 0
        except serial.serialutil.SerialException:
            print("Port {0} is unavailable!".format(self.port))
            return 1
    
    def readFromSerial(self,serial_obj):
        while True: 
            processIncomingByte(self,self.tm.read())
    
    def processIncomingByte(self,byte):
        # try loop to close this process via keyboard...
        try:
            maxBytes = 8 
            
            # terminator reached, process input line & reset thermo_output
            if byte == ">":
                temp_dict = readTempToDict(thermo_output.split(','))
                self.thermo_output = ""
            
            # if thermo_output gets too long before reaching maxBytes, 
            # reset, otherwise keep adding     
            else:     
                if len(temps) < maxBytes:
                    self.thermo_output + byte
                else: 
                    self.thermo_output = ""
                    
            return temp_dict
        
        except KeyboardInterrupt: 
            self.tm.close()
            exit()
        
        
    def readTempToDict(self,temps):            
        temp_dict = {
                    "temp_internal" : temps[0],
                    "temp_celsius" : temps[1], 
                    "temp_farenheit" : temps[2] 
                     }            

        return temp_dict      
        
    # maybe doesn't need to be a module, but need to remember to 
    # close ports when done
    def closeSerialPort(self,serial_obj):
        serial_obj.close()
            
            

                     