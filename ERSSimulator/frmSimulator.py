from PyQt5 import QtCore, QtGui, QtWidgets
from frmChuckTemp import Ui_ChuckTemp  # 導入 frmChuckTemp

class Ui_frmSimulator(object):
    def setupUi(self, frmSimulator):
        self.frmSimulator = frmSimulator  # 儲存主窗口參考
        frmSimulator.setObjectName("frmSimulator")
        frmSimulator.setEnabled(True)
        frmSimulator.resize(260, 140)
        
        # 初始化主窗口圖標和屬性
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Simulator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmSimulator.setWindowIcon(icon)
        
        self.centralwidget = QtWidgets.QWidget(frmSimulator)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        # 設定標題
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Please choose the Test")
        self.verticalLayout.addWidget(self.label)
        
        # 設定下拉選單和按鈕
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.addItem("Chuck Temp.")
        self.verticalLayout.addWidget(self.comboBox)
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setText("Continue")
        self.pushButton.clicked.connect(self.open_selected_window)  # 設定事件
        self.verticalLayout.addWidget(self.pushButton)
        
        frmSimulator.setCentralWidget(self.centralwidget)

    def open_selected_window(self):
        selected_option = self.comboBox.currentText()
        if selected_option == "Chuck Temp.":
            self.open_chuck_temp_window()

    def open_chuck_temp_window(self):
        # 創建並顯示新窗口
        self.new_window = QtWidgets.QMainWindow()
        self.ui_chuck_temp = Ui_ChuckTemp()
        self.ui_chuck_temp.setupUi(self.new_window)
        self.new_window.show()

        # 關閉當前的 frmSimulator 窗口
        self.frmSimulator.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmSimulator = QtWidgets.QMainWindow()
    ui = Ui_frmSimulator()
    ui.setupUi(frmSimulator)
    frmSimulator.show()
    sys.exit(app.exec_())
