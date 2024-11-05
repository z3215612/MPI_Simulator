import configparser
import serial

class mSetting:
    
    def mRead_RS232(self):
        # 初始化配置解析器
        config = configparser.ConfigParser()

        # 讀取Config.ini
        config.read('config.ini')
        
        # 取得Config.ini中的參數
        ComPort = config.get('RS232', 'ComPort')
        BaudRate = config.getint('RS232', 'BaudRate')
        ParityCheck = config.get('RS232', 'ParityCheck')
        StopBit = config.getint('RS232', 'StopBit')
        
        return ComPort,BaudRate,ParityCheck,StopBit
    
    def mSetting_RS232(self,ComPort,BaudRate,ParityCheck,StopBit):
        
         # 初始化配置解析器
        config = configparser.ConfigParser()
        
        # 讀取配置檔案
        config.read('config.ini')
        
        config.set('RS232', 'ComPort', ComPort)
        config.set('RS232', 'BaudRate', str(BaudRate))
        config.set('RS232', 'ParityCheck', ParityCheck)
        config.set('RS232', 'StopBit', str(StopBit))
        
        # 將更新的內容寫回配置檔案
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
            
    def mOpen_RS232(self,ComPort,BaudRate,ParityCheck,StopBit):
        self.ser = serial.Serial(
        port=ComPort,
        baudrate=BaudRate,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=1.5
        )
        
        if self.ser.is_open:
            print("串口已成功開啟")
        else:
            print("串口開啟失敗")
        
    def mClose_RS232(self):
        self.ser.close()
        
        if self.ser.is_open:
            print("串口已成功開啟")
        else:
            print("串口開啟失敗")
            
    def mSend_RS232(self,data):
        # 確認串口已開啟
        if hasattr(self, 'ser') and self.ser.is_open:
            # 發送數據，數據必須編碼成字節
            self.ser.write(data.encode('utf-8'))
            print("數據已發送:", data)
            
    def mReceive_RS232(self):
        # 確認串口已開啟
        if hasattr(self, 'ser') and self.ser.is_open:
            # 讀取指定大小的數據，並解碼
            received_data = self.ser.read(32).decode('utf-8')
            print("接收到的數據:", received_data)
            return received_data
        