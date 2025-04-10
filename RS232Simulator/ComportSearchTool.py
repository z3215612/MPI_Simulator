import serial
import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())
if len(port_list)<=0:
    print("no ports")
else:
    print("ports:")
    print(port_list)
    for comport in port_list:
        print(list(comport)[0],list(comport)[1])