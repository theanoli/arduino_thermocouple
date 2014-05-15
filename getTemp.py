#import serial 
import time

###ISSUES
# Maybe this doesn't need to be a class...?
# get clarification on self/return    



#log = 'temp_log.txt'    # for testing purposes
#open(log,'wb').close()

        
class getSensorData():
    def __init__(self,log):
        self.port = 'COM3'
        # Setting timeout to 0 opens port in non-blocking mode; None waits forever
        self.tm = serial.Serial(None, 9600, timeout=None)
        #self.log = log 
        
    def checkPortAvailability(self):
        try: 
            self.tm.open(self.port)
            return 0
        except serial.serialutil.SerialException:
            self.err = "Port {0} is unavailable!".format(self.port)
            return 1
        
    
    def processIncomingByte(self,byte):
        # try loop to close this process via keyboard during testing...
        try:
            maxBytes = 8 
            
            # terminator reached, process output line & reset sensor_output
            if byte == ">":
                sensor_output = sensor_output.split('!')
                temp = sensor_output[0]
                flow = sensor_output[1]
                
                temp_dict = readTempToDict(temp.split(','))
                flow_dict = readFlowToDict(flow)
                
                sensor_output = ""
            
            # if sensor_output gets too long before reaching maxBytes, 
            # reset, otherwise keep adding     
            else:     
                if len(temps) < maxBytes:
                    sensor_output + byte
                else: 
                    sensor_output = ""
                    
            return temp_dict,flow_dict
        
        except KeyboardInterrupt: 
            self.tm.close()
            exit()
        
    
    def readTempToDict(self,temp_list):            
        temp_dict = {
                    "temp_internal" : temp_list[0],
                    "temp_celsius" : temp_list[1], 
                    "temp_farenheit" : temp_list[2] 
                     }            

        return temp_dict   
    
    def readFlowToDict(self,flow):
        flow_dict = {"flow" : flow}   
        return flow_dict


    def readFromSerial(self,serial_obj):
        temp_dict,flow_dict = processIncomingByte(self,self.tm.read())
        return temp_dict,flow_dict

        
    # maybe doesn't need to be a module, but need to remember to 
    # close ports when done
    def closeSerialPort(self,serial_obj):
        serial_obj.close()
            
            

                     