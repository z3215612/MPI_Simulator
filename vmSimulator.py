from mSimulator import mSetting

class vmSetting:
    
    def __init__(self):       
        self.Setting=mSetting()
    
    def getSetting(self):
        return self.Setting
    
    def vmRead_RS232(self):
        
        ComPort,BaudRate,ParityCheck,StopBit = self.Setting.mRead_RS232()
        return ComPort,BaudRate,ParityCheck,StopBit
    
    def vmSetting_RS232(self,ComPort,BaudRate,ParityCheck,StopBit):       
        self.Setting.mSetting_RS232(ComPort,BaudRate,ParityCheck,StopBit)
        
    def vmOpen_RS232(self,ComPort,BaudRate,ParityCheck,StopBit):       
        self.Setting.mOpen_RS232(ComPort,BaudRate,ParityCheck,StopBit)
    
    def vmClose_RS232(self):
        self.Setting.mClose_RS232()
        
class vmChucktemp:
    
    def __init__(self,Setting = mSetting):
        self.setting = Setting
    
    def vmSenddata_RS232(self,data):
        self.setting.mSend_RS232(data)
        
    def vmReceive_RS232(self):
        self.setting.mReceive_RS232()
        data = self.setting.mReceive_RS232
        return data