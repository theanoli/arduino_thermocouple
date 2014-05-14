from getTemp import *

F = getTemp()


if F.checkIfAvailable() == 0:
    temp_dict = F.readFromSerial(F.checkIfAvailable().tm)
    print(temp_dict)
else: 
    print("something wrong with your ports!")