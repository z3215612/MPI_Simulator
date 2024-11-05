from PyQt5 import QtCore, QtGui, QtWidgets
from vmSimulator import vmSetting,vmChucktemp
import threading
import time

class Ui_ChuckTemp(object):
    
    def __init__(self):
        self.Setting=vmSetting()
        self.Data=vmChucktemp(self.Setting.getSetting())
        self.received_data = ""  # 用來儲存接收到的資料
        self.keep_receiving = True  # 控制執行緒的運行狀態
        
    def setupUi(self, frmChuckTemp):
        frmChuckTemp.setObjectName("frmChuckTemp")
        frmChuckTemp.setEnabled(True)
        frmChuckTemp.resize(575, 275)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmChuckTemp.sizePolicy().hasHeightForWidth())
        frmChuckTemp.setSizePolicy(sizePolicy)
        frmChuckTemp.setMinimumSize(QtCore.QSize(575, 275))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Simulator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmChuckTemp.setWindowIcon(icon)
        self.centralwidget_ChuckTemp = QtWidgets.QWidget(frmChuckTemp)
        self.centralwidget_ChuckTemp.setObjectName("centralwidget_ChuckTemp")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget_ChuckTemp)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 501, 171))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_ChuckTemp = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_ChuckTemp.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_ChuckTemp.setObjectName("verticalLayout_ChuckTemp")
        self.horizontalLayout_Temp = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Temp.setObjectName("horizontalLayout_Temp")
        self.Label_Temp = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Label_Temp.setFont(font)
        self.Label_Temp.setObjectName("Label_Temp")
        self.horizontalLayout_Temp.addWidget(self.Label_Temp)
        self.lineEdit_Temp = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Temp.sizePolicy().hasHeightForWidth())
        self.lineEdit_Temp.setSizePolicy(sizePolicy)
        self.lineEdit_Temp.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Temp.setFont(font)
        self.lineEdit_Temp.setObjectName("lineEdit_Temp")
        self.horizontalLayout_Temp.addWidget(self.lineEdit_Temp)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Temp.addItem(spacerItem)
        self.verticalLayout_ChuckTemp.addLayout(self.horizontalLayout_Temp)
        self.horizontalLayout_CS = QtWidgets.QHBoxLayout()
        self.horizontalLayout_CS.setObjectName("horizontalLayout_CS")
        self.horizontalLayout_Com = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Com.setObjectName("horizontalLayout_Com")
        self.Label_Com = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Com.setFont(font)
        self.Label_Com.setObjectName("Label_Com")
        self.horizontalLayout_Com.addWidget(self.Label_Com)
        self.lineEdit_ComPort = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ComPort.sizePolicy().hasHeightForWidth())
        self.lineEdit_ComPort.setSizePolicy(sizePolicy)
        self.lineEdit_ComPort.setMinimumSize(QtCore.QSize(40, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_ComPort.setFont(font)
        self.lineEdit_ComPort.setObjectName("lineEdit_ComPort")
        self.horizontalLayout_Com.addWidget(self.lineEdit_ComPort)
        self.horizontalLayout_CS.addLayout(self.horizontalLayout_Com)
        spacerItem1 = QtWidgets.QSpacerItem(475, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_CS.addItem(spacerItem1)
        self.Label_Status = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Label_Status.setFont(font)
        self.Label_Status.setStyleSheet("background-color: red; \n"
"color: black; ")
        self.Label_Status.setObjectName("Label_Status")
        self.horizontalLayout_CS.addWidget(self.Label_Status)
        self.verticalLayout_ChuckTemp.addLayout(self.horizontalLayout_CS)
        self.horizontalLayout_BPS = QtWidgets.QHBoxLayout()
        self.horizontalLayout_BPS.setObjectName("horizontalLayout_BPS")
        self.horizontalLayout_BaudRate = QtWidgets.QHBoxLayout()
        self.horizontalLayout_BaudRate.setObjectName("horizontalLayout_BaudRate")
        self.Label_BaudRate = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_BaudRate.setFont(font)
        self.Label_BaudRate.setObjectName("Label_BaudRate")
        self.horizontalLayout_BaudRate.addWidget(self.Label_BaudRate)
        self.lineEdit_BaudRate = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_BaudRate.sizePolicy().hasHeightForWidth())
        self.lineEdit_BaudRate.setSizePolicy(sizePolicy)
        self.lineEdit_BaudRate.setMinimumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_BaudRate.setFont(font)
        self.lineEdit_BaudRate.setObjectName("lineEdit_BaudRate")
        self.horizontalLayout_BaudRate.addWidget(self.lineEdit_BaudRate)
        self.horizontalLayout_BPS.addLayout(self.horizontalLayout_BaudRate)
        self.horizontalLayout_ParityCheck = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ParityCheck.setObjectName("horizontalLayout_ParityCheck")
        self.Label_ParityCheck = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_ParityCheck.setFont(font)
        self.Label_ParityCheck.setObjectName("Label_ParityCheck")
        self.horizontalLayout_ParityCheck.addWidget(self.Label_ParityCheck)
        self.lineEdit_ParityCheck = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ParityCheck.sizePolicy().hasHeightForWidth())
        self.lineEdit_ParityCheck.setSizePolicy(sizePolicy)
        self.lineEdit_ParityCheck.setMinimumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_ParityCheck.setFont(font)
        self.lineEdit_ParityCheck.setObjectName("lineEdit_ParityCheck")
        self.horizontalLayout_ParityCheck.addWidget(self.lineEdit_ParityCheck)
        self.horizontalLayout_BPS.addLayout(self.horizontalLayout_ParityCheck)
        self.horizontalLayout_StopBit = QtWidgets.QHBoxLayout()
        self.horizontalLayout_StopBit.setObjectName("horizontalLayout_StopBit")
        self.Label_StopBit = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Label_StopBit.setFont(font)
        self.Label_StopBit.setObjectName("Label_StopBit")
        self.horizontalLayout_StopBit.addWidget(self.Label_StopBit)
        self.lineEdit_StopBit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_StopBit.sizePolicy().hasHeightForWidth())
        self.lineEdit_StopBit.setSizePolicy(sizePolicy)
        self.lineEdit_StopBit.setMinimumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_StopBit.setFont(font)
        self.lineEdit_StopBit.setObjectName("lineEdit_StopBit")
        self.horizontalLayout_StopBit.addWidget(self.lineEdit_StopBit)
        self.horizontalLayout_BPS.addLayout(self.horizontalLayout_StopBit)
        self.verticalLayout_ChuckTemp.addLayout(self.horizontalLayout_BPS)
        self.horizontalLayout_Send = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Send.setObjectName("horizontalLayout_Send")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Send.addItem(spacerItem2)
        
        self.PushButton_Set = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_Set.sizePolicy().hasHeightForWidth())
        self.PushButton_Set.setSizePolicy(sizePolicy)
        self.PushButton_Set.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.PushButton_Set.setFont(font)
        self.PushButton_Set.setObjectName("PushButton_Set")
        self.horizontalLayout_Send.addWidget(self.PushButton_Set)
        self.PushButton_Set.clicked.connect(self.setting_values)
        
        self.PushButton_Send = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PushButton_Send.sizePolicy().hasHeightForWidth())
        self.PushButton_Send.setSizePolicy(sizePolicy)
        self.PushButton_Send.setMinimumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.PushButton_Send.setFont(font)
        self.PushButton_Send.setObjectName("PushButton_Send")
        self.horizontalLayout_Send.addWidget(self.PushButton_Send)
        self.verticalLayout_ChuckTemp.addLayout(self.horizontalLayout_Send)
        frmChuckTemp.setCentralWidget(self.centralwidget_ChuckTemp)
        self.PushButton_Send.clicked.connect(self.send_RS232)

        self.retranslateUi(frmChuckTemp)
        QtCore.QMetaObject.connectSlotsByName(frmChuckTemp)
        
        self.read_values()
        self.open_RS232()
        
        # 啟動資料接收執行緒
        self.start_data_receiving_thread()

## 使用 QTimer 定期更新 UI 顯示接收到的資料
#self.timer = QtCore.QTimer()
#self.timer.timeout.connect(self.update_received_data)
#self.timer.start(500)  # 每 500 毫秒更新一次

        self.retranslateUi(frmChuckTemp)
        QtCore.QMetaObject.connectSlotsByName(frmChuckTemp)
        
    def retranslateUi(self, frmChuckTemp):
        _translate = QtCore.QCoreApplication.translate
        frmChuckTemp.setWindowTitle(_translate("frmChuckTemp", "Chuck Temp."))
        self.Label_Temp.setText(_translate("frmChuckTemp", "Temp."))
        self.Label_Com.setText(_translate("frmChuckTemp", "ComPort"))
        self.Label_Status.setText(_translate("frmChuckTemp", "Disconnect"))
        self.Label_BaudRate.setText(_translate("frmChuckTemp", "Baud Rate"))
        self.Label_ParityCheck.setText(_translate("frmChuckTemp", "Parity Check"))
        self.Label_StopBit.setText(_translate("frmChuckTemp", "Stop Bit"))
        self.PushButton_Set.setText(_translate("frmChuckTemp", "Set"))
        self.PushButton_Send.setText(_translate("frmChuckTemp", "Send"))
    
    def read_values(self):
        
        ComPort, BaudRate, ParityCheck, StopBit = self.Setting.vmRead_RS232()
        
        self.lineEdit_ComPort.setText(ComPort)
        self.lineEdit_BaudRate.setText(str(BaudRate))
        self.lineEdit_ParityCheck.setText(ParityCheck)
        self.lineEdit_StopBit.setText(str(StopBit))

    def setting_values(self):
        
        self.Setting.vmClose_RS232()

        ComPort = self.lineEdit_ComPort.text()
        BaudRate = self.lineEdit_BaudRate.text()
        ParityCheck = self.lineEdit_ParityCheck.text()
        StopBit = self.lineEdit_StopBit.text()
        
        self.Setting.vmSetting_RS232(ComPort,BaudRate,ParityCheck,StopBit)
        self.Setting.vmOpen_RS232(ComPort,BaudRate,ParityCheck,StopBit)  
    
    def open_RS232(self):
                
        ComPort = self.lineEdit_ComPort.text()
        BaudRate = self.lineEdit_BaudRate.text()
        ParityCheck = self.lineEdit_ParityCheck.text()
        StopBit = self.lineEdit_StopBit.text()
        
        self.Setting.vmOpen_RS232(ComPort,BaudRate,ParityCheck,StopBit)
        
    def send_RS232(self):
        Temp = self.lineEdit_Temp.text()
        
        self.Data.vmSenddata_RS232(Temp)
        
    def receive_RS232(self):
        
        if self.Data.vmReceive_RS232() != "":
            
            Temp = self.Data.vmReceive_RS232()
        
            self.lineEdit_Temp.text = Temp
    
    def start_data_receiving_thread(self):
        # 建立並啟動接收資料的執行緒
        self.receive_thread = threading.Thread(target=self.receive_data_loop)
        self.receive_thread.daemon = True  # 設定為背景執行緒
        self.receive_thread.start()
    
    def receive_data_loop(self):
        # 執行緒不斷檢查資料
        while self.keep_receiving:
            data = self.Data.vmReceive_RS232()
            if data:
                self.received_data = data  # 若有資料，儲存到 received_data
            time.sleep(0.5)  # 延遲以避免頻繁檢查
    
    def update_received_data(self):
        # 更新 UI 顯示接收到的資料
        if self.received_data:
            self.lineEdit_Temp.setText(self.received_data)
            self.received_data = ""  # 清空已顯示的資料
    
    def closeEvent(self, event):
        # 停止接收執行緒
        self.keep_receiving = False
        self.receive_thread.join()
        event.accept()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmChuckTemp = QtWidgets.QMainWindow()
    ui = Ui_ChuckTemp()
    ui.setupUi(frmChuckTemp)
    frmChuckTemp.show()
    sys.exit(app.exec_())
