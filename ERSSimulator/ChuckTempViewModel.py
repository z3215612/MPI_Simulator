from SettingModel import mSetting

class vmChucktemp:
    
    def __init__(self,Setting = mSetting):
        self.setting = Setting
        self.RAM = "0"
        self.SH = "0"
        self.RO = "0"
        self.SPA = "0"
        self.OK = "OK"
        self.rn = "\r\n"
        self.compensation_tables = {
            1: [[None, None] for _ in range(10)],  # list 1
            2: [[None, None] for _ in range(10)],  # list 2
            3: [[None, None] for _ in range(10)]   # list 3
        }
        self.temporary_storage_tables = {
            1: [[None, None] for _ in range(10)]
        }
        self.SCswitch = False

    def vmSenddata_RS232(self,data):
        self.setting.mSend_RS232(data)
            
    def vmSendRTdata_RS232(self,data):
        
        #Determine the sign       
        sign = "+" if data >= 0 else "-"
        
        integer_value = abs(data) * 10
        
        data = f"T{sign}{int(integer_value):04d}"  #4 digit zero padding
        self.setting.mSend_RS232(str(data) + self.rn)
        
    def vmSendRcdata_RS232(self,data):
        
        if self.SCswitch == True:
            
            data = self.TemperatureCompensation(data)
            
        #Determine the sign
        sign = "+" if data >= 0 else "-"
        
        integer_value = abs(data) * 10
        
        data = f"C{sign}{int(integer_value):04d}"  #4 digit zero padding
                  
        self.setting.mSend_RS232(str(data) + self.rn)

    def vmReceive_RS232(self):
        data = self.setting.mReceive_RS232()
        
        #request actual temperature
        
        if data[:2] == "Rc":        
        
            return data
        
        #request set temperature
        
        elif data[:2] == "RT":
            return data
            
        elif data[:3] == "RL0":
            self.setting.mSend_RS232("L0" + self.rn)
            
        elif data[:2] == "RR":
            self.setting.mSend_RS232("R+00-00" + self.rn)
            
        elif data[:2] == "RD":
            self.setting.mSend_RS232("D1" + self.rn)
            
        elif data[:2] == "RE":
            self.setting.mSend_RS232("E000" + self.rn)
            
        elif data[:2] == "RI":
            self.setting.mSend_RS232("I0" + self.rn)
            
        elif data[:2] == "RM":
            self.setting.mSend_RS232("M-1000+3000" + self.rn)
                
        elif data[:3] == "RSE":
            self.setting.mSend_RS232("SE1" + self.rn)
            
        elif data[:3] == "RHM":
            self.setting.mSend_RS232("HM0" + self.rn)
            
        elif data[:3] == "RPA":
            self.setting.mSend_RS232("PA0" + self.rn)
            
        elif data[:3] == "RCM":
            self.setting.mSend_RS232("CM0" + self.rn)
            
        elif data[:3] == "RVB":
            self.setting.mSend_RS232("VB1234567" + self.rn)
        
        #set hold mode
        
        elif data[:2] == "SH":
            
            self.SH = data[2]
            
            self.setting.mSend_RS232(self.OK + self.rn)
            
        #request status of high purge
                
        elif data[:3] == "RHP":
            
            self.setting.mSend_RS232("HP" + self.SPA + self.rn)
            
        #request status of hold mode    
            
        elif data[:2] == "RH":
            self.setting.mSend_RS232("H" + self.SH + self.rn)
            
        #set operating mode
            
        elif data[:2] == "SO":
            if data[2] == "1":
                self.RO = data[2] 
            
            elif data[2] == "2":
                self.RO = data[2]
            
            elif data[2] == "3":
                self.RO = data[2]
            
            elif data[2] == "5":
                self.RAM = "1"
                
            elif data[2] == "6":
                self.RAM = "0"
                
            self.setting.mSend_RS232(" " + self.rn)
            
        #request operation mode
        
        elif data[:2] == "RO":
            self.setting.mSend_RS232("O" + self.RO + self.rn)
        
        #set airflow mode
        
        elif data[:3] == "SAM":
            
            if data[2] == "5":
                self.RAM = "1"
                
            elif data[2] == "6":
                self.RAM = "0"
        
        #request for airflow mode
        
        elif data[:3] == "RAM":
                self.setting.mSend_RS232("AM" + self.RAM + self.rn)
        
        #set high power air mode
        
        elif data[:3] == "SPA":
            self.SPA = data[3]
            
            self.setting.mSend_RS232(self.OK + self.rn)
            
        #set new set temperature
            
        elif data[:2] == "ST":
            
            sign = ""

            if data[2] == "-":
                sign = data[2]

            number = data[3:]

            data = f"{sign}{int(number) / 10 :.1f}"

            self.setting.mSend_RS232(" " + self.rn)

            return data
        
        elif data[:3] == "SCI":
            
            self.SCI = data[3]
            self.temporary_storage_tables[1] = self.compensation_tables[int(self.SCI)]
            print(self.temporary_storage_tables[1])
            
        elif data[:3] == "SCT":
            
            self.SCT = data[3]
            self.SCswitch = True
            
        elif data[:3] == "SCP":
        
           self.temporary_storage_tables[1][int(data[3])][0] = float(data[4:9]) / 10.0
           self.temporary_storage_tables[1][int(data[3])][1] = float(data[9:]) / 10.0
        
        elif data[:3] == "SCS":
            
            self.compensation_tables[int(self.SCI)] = self.temporary_storage_tables[1]
            print(self.compensation_tables[int(self.SCI)])
            return self.SCI
        
        elif data[:3] == "SCC":
        
            self.SCswitch = False
            
    def TemperatureCompensation(self,temp):
        
        for row in self.compensation_tables[int(self.SCT)]:
            if row[0] == temp:
                temp = row[1]
                return temp
                