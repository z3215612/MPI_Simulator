import serial, time 
ser = serial.Serial()
ser.port = "COM2"  
#115200,N,8,1
ser.baudrate = 19200
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check
ser.stopbits = serial.STOPBITS_ONE #number of stop bits  
ser.timeout = 0.5          #non-block read 0.5s
ser.writeTimeout = 0.5     #timeout for write 0.5s
ser.xonxoff = False    #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False     #disable hardware (DSR/DTR) flow control
data = " "  
try: 
    ser.open()
except Exception as ex:
    print ("open serial port error " + str(ex))
    exit()
  
if ser.isOpen():  
    try:
        ser.flushInput() #flush input buffer
        ser.flushOutput() #flush output buffer
        
        ser.write([35, 48, 50, 49, 48, 48, 48, 13])
        ser.write([35, 48, 50, 49, 49, 48, 49, 13])
        ser.write([35, 48, 50, 49, 50, 48, 49, 13])
        ser.write([35, 48, 50, 49, 52, 48, 48, 13])
        ser.write([35, 48, 50, 49, 51, 48, 48, 13])
        ser.write([35, 48, 50, 49, 53, 48, 49, 13])
        ser.write([36, 48, 50, 54, 13])
        
        #print("write 8 byte data: 36, 48, 50, 77,13")
        while True:
            data = ser.read(8)
            print (data)
    except Exception as e1:
        print ("communicating error " + str(e1))
else:
    print ("open serial port error")