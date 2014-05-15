import getTemp

F = getSensorData()
portAvailability = F.checkPortAvailability()


if portAvailability == 0:
    while True: 
        temp_dict,flow_dict = F.readFromSerial(F.tm)
        print(["%s: %s\t" % (key,temp_dict[key]) for key in temp_dict] + "\n")
        print(flow_dict["flow"] + "\n\n")
else: 
    print(portAvailability.err)