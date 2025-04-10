from PyQt5 import QtCore, QtGui, QtWidgets
from ChuckTempViewModel import vmChucktemp
from SettingViewModel import vmSetting
import threading
import time

class Ui_ChuckTemp(object):
        
    def __init__(self):
            
        self.Setting = vmSetting()
        self.Data = vmChucktemp(self.Setting.getSetting())
        self.received_data = ""  #used to store received data
        self.keep_receiving = True  #Control the running status of execution threads

    def setupUi(self, frmChuckTemp):
                
        frmChuckTemp.setObjectName("frmChuckTemp")
        frmChuckTemp.setEnabled(True)
        frmChuckTemp.resize(575, 385)
        icon = QtGui.QIcon("Simulator.png")
        frmChuckTemp.setWindowIcon(icon)
        frmChuckTemp.setWindowTitle("ERSSimulator")

        self.tab_widget = QtWidgets.QTabWidget(frmChuckTemp)
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 575, 400))

        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setObjectName("MainTab")
        self.setup_MainTab(self.MainTab)
        self.tab_widget.addTab(self.MainTab, "Main")

        self.TempCompensateTab = QtWidgets.QWidget()
        self.TempCompensateTab.setObjectName("TempCompensateTab")
        self.setup_TempCompensateTab(self.TempCompensateTab)
        self.tab_widget.addTab(self.TempCompensateTab, "TempCompensate")
        
        self.read_values()
        self.open_RS232()
        self.start_data_receiving_thread()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_received_data)
        self.timer.start(500)

    def setup_MainTab(self, tab):
                
        layoutWidget = QtWidgets.QWidget(tab)
        layoutWidget.setGeometry(QtCore.QRect(10, 50, 500, 170))

        verticalLayout = QtWidgets.QVBoxLayout(layoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)

        # Temperature Controls
        horizontalLayout_Temp = QtWidgets.QHBoxLayout()
        self.Label_Temp = QtWidgets.QLabel("Temp.", layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.Label_Temp.setFont(font)
        horizontalLayout_Temp.addWidget(self.Label_Temp)

        self.lineEdit_Temp = QtWidgets.QLineEdit(layoutWidget)
        self.lineEdit_Temp.setMinimumSize(QtCore.QSize(150, 30))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Temp.setFont(font)
        horizontalLayout_Temp.addWidget(self.lineEdit_Temp)

        horizontalLayout_Temp.addSpacerItem(QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        verticalLayout.addLayout(horizontalLayout_Temp)

        # Communication Port Controls
        horizontalLayout_Com = QtWidgets.QHBoxLayout()
        self.Label_Com = QtWidgets.QLabel("ComPort", layoutWidget)
        font.setPointSize(12)
        self.Label_Com.setFont(font)
        horizontalLayout_Com.addWidget(self.Label_Com)

        self.lineEdit_ComPort = QtWidgets.QLineEdit(layoutWidget)
        self.lineEdit_ComPort.setMinimumSize(QtCore.QSize(60, 30))
        self.lineEdit_ComPort.setFont(font)
        horizontalLayout_Com.addWidget(self.lineEdit_ComPort)

        horizontalLayout_Com.addSpacerItem(QtWidgets.QSpacerItem(475, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))
        verticalLayout.addLayout(horizontalLayout_Com)

        # Buttons
        horizontalLayout_Send = QtWidgets.QHBoxLayout()
        horizontalLayout_Send.addSpacerItem(QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum))

        self.PushButton_Set = QtWidgets.QPushButton("Set", layoutWidget)
        self.PushButton_Set.setMinimumSize(QtCore.QSize(40, 40))
        font.setPointSize(15)
        self.PushButton_Set.setFont(font)
        horizontalLayout_Send.addWidget(self.PushButton_Set)
        self.PushButton_Set.clicked.connect(self.setting_values)

        self.PushButton_Send = QtWidgets.QPushButton("Send", layoutWidget)
        self.PushButton_Send.setMinimumSize(QtCore.QSize(40, 40))
        self.PushButton_Send.setFont(font)
        horizontalLayout_Send.addWidget(self.PushButton_Send)
        self.PushButton_Send.clicked.connect(self.send_RS232)

        verticalLayout.addLayout(horizontalLayout_Send)

    def setup_TempCompensateTab(self, tab):
        
        self.nested_tab_widget = QtWidgets.QTabWidget(tab)
        self.nested_tab_widget.setGeometry(QtCore.QRect(10, 10, 700, 350))
        self.nested_tab_widget.setObjectName("nested_tab_widget")

        # 第一個子 Tab
        self.nested_tab1 = QtWidgets.QWidget()
        self.nested_tab1.setObjectName("TempCompensateTable1")
        self.setup_TempCompensateTab1(self.nested_tab1)
        self.nested_tab_widget.addTab(self.nested_tab1, "TempCompensateTable1")

        # 第二個子 Tab
        self.nested_tab2 = QtWidgets.QWidget()
        self.nested_tab2.setObjectName("TempCompensateTable2")
        self.setup_TempCompensateTab2(self.nested_tab2)
        self.nested_tab_widget.addTab(self.nested_tab2, "TempCompensateTable2")

        # 第三個子 Tab
        self.nested_tab3 = QtWidgets.QWidget()
        self.nested_tab3.setObjectName("TempCompensateTable3")
        self.setup_TempCompensateTab3(self.nested_tab3)
        self.nested_tab_widget.addTab(self.nested_tab3, "TempCompensateTable3")
    
    def setup_TempCompensateTab1(self, tab):
        
        self.table_widget1 = QtWidgets.QTableWidget(tab)
        self.table_widget1.setGeometry(QtCore.QRect(10, 10, 350, 300))  # 設置表格大小
        self.table_widget1.verticalHeader().setVisible(False)
        self.table_widget1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget1.setRowCount(10)  # 設置行數
        self.table_widget1.setColumnCount(3)  # 設置列數
        self.table_widget1.setHorizontalHeaderLabels(["Index", "Origin", "Compensate"])  # 設置標題

        # 填充初始數據
        for row in range(10):
            self.table_widget1.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{row}"))
            self.table_widget1.setItem(row, 1, QtWidgets.QTableWidgetItem("None"))
            self.table_widget1.setItem(row, 2, QtWidgets.QTableWidgetItem("None"))
            
    def setup_TempCompensateTab2(self, tab):
        
        self.table_widget2 = QtWidgets.QTableWidget(tab)
        self.table_widget2.setGeometry(QtCore.QRect(10, 10, 350, 300))  # 設置表格大小
        self.table_widget2.verticalHeader().setVisible(False)
        self.table_widget2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget2.setRowCount(10)  # 設置行數
        self.table_widget2.setColumnCount(3)  # 設置列數
        self.table_widget2.setHorizontalHeaderLabels(["Index", "Origin", "Compensate"])  # 設置標題

        # 填充初始數據
        for row in range(10):
            self.table_widget2.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{row}"))
            self.table_widget2.setItem(row, 1, QtWidgets.QTableWidgetItem("None"))
            self.table_widget2.setItem(row, 2, QtWidgets.QTableWidgetItem("None"))
            
    def setup_TempCompensateTab3(self, tab):
        
        self.table_widget3 = QtWidgets.QTableWidget(tab)
        self.table_widget3.setGeometry(QtCore.QRect(10, 10, 350, 300))  # 設置表格大小
        self.table_widget3.verticalHeader().setVisible(False)
        self.table_widget3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget3.setRowCount(10)  # 設置行數
        self.table_widget3.setColumnCount(3)  # 設置列數
        self.table_widget3.setHorizontalHeaderLabels(["Index", "Origin", "Compensate"])  # 設置標題

        # 填充初始數據
        for row in range(10):
            self.table_widget3.setItem(row, 0, QtWidgets.QTableWidgetItem(f"{row}"))
            self.table_widget3.setItem(row, 1, QtWidgets.QTableWidgetItem("None"))
            self.table_widget3.setItem(row, 2, QtWidgets.QTableWidgetItem("None"))

    def read_values(self):
        
        ComPort = self.Setting.vmRead_RS232()
        self.lineEdit_ComPort.setText(ComPort)

    def setting_values(self):
        
        self.Setting.vmClose_RS232()
        ComPort = self.lineEdit_ComPort.text()
        self.Setting.vmSetting_RS232(ComPort)
        self.Setting.vmOpen_RS232(ComPort)

    def open_RS232(self):
        
        ComPort = self.lineEdit_ComPort.text()
        self.Setting.vmOpen_RS232(ComPort)

    def send_RS232(self):
        
        Temp = self.lineEdit_Temp.text()
        self.Data.vmSenddata_RS232(Temp)

    def start_data_receiving_thread(self):
        
        self.receive_thread = threading.Thread(target=self.receive_data_loop)
        self.receive_thread.daemon = True
        self.receive_thread.start()

    def receive_data_loop(self):
        
        while self.keep_receiving:
            data = self.Data.vmReceive_RS232()
            if str(data)[:2] == "RT":
                Temp = self.lineEdit_Temp.text() or "25.0"
                self.received_data = Temp
                self.Data.vmSendRTdata_RS232(float(Temp))

            elif str(data)[:2] == "Rc":
                Temp = self.lineEdit_Temp.text() or "25.0"
                self.received_data = Temp
                self.Data.vmSendRcdata_RS232(float(Temp))

            elif str(data) == "1":
                
                for row in range(10):
                    
                    self.table_widget1.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.Data.compensation_tables[1][row][0])))
                    self.table_widget1.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.Data.compensation_tables[1][row][1])))
                    self.table_widget1.viewport().update()
                
            elif str(data) == "2":
                
                for row in range(10):
                    
                    self.table_widget2.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.Data.compensation_tables[2][row][0])))
                    self.table_widget2.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.Data.compensation_tables[2][row][1])))
                    self.table_widget2.viewport().update()
                    
            elif str(data) == "3":
                
                for row in range(10):
                    
                    self.table_widget3.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.Data.compensation_tables[3][row][0])))
                    self.table_widget3.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.Data.compensation_tables[3][row][1])))
                    self.table_widget3.viewport().update()
            
            elif data:
                self.received_data = data
                
            time.sleep(0.5)

    def update_received_data(self):
        
        if self.received_data:
            self.lineEdit_Temp.setText(str(self.received_data))
            self.received_data = ""

    def closeEvent(self, event):
        
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
