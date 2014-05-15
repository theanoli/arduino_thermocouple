from getTemp import *

F = getTemp()
portAvailability = F.checkPortAvailability()


if portAvailability == 0:
    while True: 
        temp_dict = F.readFromSerial(F.tm)
        print([temp_dict[key]+"\t" for key in temp_dict])
        print("\n")
else: 
    print(portAvailability.err)