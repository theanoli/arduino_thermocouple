#import serial 
import time

###ISSUES
# how to get this to talk to the DB
# what if the port is unavailable?
# how to log: with image metadata (i.e, each image gets a set of temp
#    readings? 
# Or log separate from image metadata, combine this with the images
#    later?
# 


log = 'temp_log.txt'
open(log,'wb').close()

        
class getTemp():
    def __init__(self, tm):
        self.port = 'COM3'
        self.log = 'temp_log.txt'
        self.tm = None
        
    def checkIfAvailable(self):
        try: 
            self.tm = serial.Serial(self.port, 9600, timeout=0)
            return 0
        except serial.serialutil.SerialException:
            print("Port {0} is unavailable!".format(self.port))
            return 1
    
    # read to console with timestamp
    def readTempToConsole(self):
        temp_dict = {"temp_internal" : [],
                     "temp_celsius" : [],
                     "temp_farenheit" : []
                     "temp_timer" : []}
        while True: 
            try: 
                self.tm.write("ping")
                
                temps = [t.decode().strip() for t in self.tm.readlines()]
                temp_dict["temp_internal"].append(temps[0])
                temp_dict["temp_celsius"].append(temps[1])
                temp_dict["temp_farenheit"].append(temps[2])
                temp_dict["temp_timer"].append(time.time())
                
                self.tm.flush()
                
                time.sleep(5)

            except KeyboardInterrupt: 
                self.tm.close()
                exit()
                
        
    # maybe doesn't need to be a module, but need to remember to 
    # close ports when done
    def closeSerialPort(self,port_obj):
        port_obj.close()
            
                     