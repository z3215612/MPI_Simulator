from SettingModel import mSetting

class vmSetting:
    
    def __init__(self):       
        self.Setting=mSetting()
    
    def getSetting(self):
        return self.Setting
    
    def vmRead_RS232(self):
        
        ComPort = self.Setting.mRead_RS232()
        return ComPort
    
    def vmSetting_RS232(self,ComPort):
        self.Setting.mSetting_RS232(ComPort)
        
    def vmOpen_RS232(self,ComPort):
        self.Setting.mOpen_RS232(ComPort)
    
    def vmClose_RS232(self):
        self.Setting.mClose_RS232()
