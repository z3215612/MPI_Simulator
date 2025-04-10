import serial
import SwapBridgeSimulator
import HardwareHandler
import configparser
import threading

config = configparser.ConfigParser()
# read config
config.read('config.ini', encoding='utf-8')
ComPort = config['info']['ComPort']
BaudRate = config['info']['BaudRate']
Simulator = config['info']['Simulator']
ser = serial.Serial(ComPort,BaudRate,timeout = 0.5)
temp =''


def main():
    #Open Serial port
    if ser.isOpen():
        print ("Connect Success")
    else:
        print ("Connect Failed")
    #Set initial status  
    InitialStatus = HardwareHandler.InitialHardware(Simulator)
    #Run Simulator
    if InitialStatus:
        SMThread = threading.Thread(target = StartSimulator)
        SMThread.start()
        HardwareHandler.SimulatorGUI(Simulator)

def StartSimulator():
    decoded_string = ""
    HardwareReturn = ""
    while True:
        try:
            data = ser.read(1)
            decoded_string =decoded_string + data.decode("utf-8")
            if data.decode("utf-8") == "\r":
                HardwareReturn = HardwareHandler.GetHardwareReturn(Simulator,decoded_string)
                decoded_string = ""
                if (HardwareReturn !=""):
                    ser.write(HardwareReturn)
        except Exception as e:
            print(e)
        
if __name__=="__main__":
    main()       
 
        
        

