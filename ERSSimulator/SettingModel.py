import configparser
import serial

class mSetting:
    
    def mRead_RS232(self):

        config = configparser.ConfigParser()

        config.read('config.ini')
        
        ComPort = config.get('RS232', 'ComPort')
        
        return ComPort
    
    def mSetting_RS232(self,ComPort):
        
        config = configparser.ConfigParser()
        
        config.read('config.ini')
        
        config.set('RS232', 'ComPort', ComPort)
        
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
            
    def mOpen_RS232(self,ComPort):
        self.ser = serial.Serial(
        port=ComPort,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1.5
        )
        
        if self.ser.is_open:
            print("Serial port has been successfully opened.")
        else:
            print("Serial port opening failed.")
        
    def mClose_RS232(self):
        self.ser.close()
        
        if self.ser.is_open:
            print("Failed to close serial port.")
        else:
            print("Serial port closed successfully.")
            
    def mSend_RS232(self,data):
        
        #confirm that the serial port is open
        if hasattr(self, 'ser') and self.ser.is_open:
            
            self.ser.write(data.encode('utf-8'))
            print("Data has been sent:", data)
            
    def mReceive_RS232(self):
        
        #confirm that the serial port is open
        if hasattr(self, 'ser') and self.ser.is_open:

            end_marker = '\r\n'
            received_data = self.ser.read_until(end_marker.encode('utf-8')).decode('utf-8')
            
            if received_data:
                print("Data received:", received_data)
                
            else:
                print("No data")
                
            return received_data
