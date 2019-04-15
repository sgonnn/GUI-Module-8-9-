import sys
import qdarkstyle
from PyQt5 import QtWidgets ,QtGui , QtCore
from PyQt5.QtWidgets import QPushButton , QLabel , QLineEdit , QGroupBox , QSpinBox , QHBoxLayout , QGridLayout
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # creating EmailBlast widget and setting it as central
        self.Window_widget = SR()
        self.setCentralWidget(self.Window_widget)

        # filling up a menu bar
        bar = self.menuBar()

        # Mode menu
        mode_menu = bar.addMenu('  Mode  ')

        # adding actions to file menu
        st_action = QtWidgets.QAction('Start', self)
        SR_action = QtWidgets.QAction('Search&Receive', self)
        Man_action = QtWidgets.QAction('Manual Control', self)
        RESET_action = QtWidgets.QAction('Reset', self)
        close_action = QtWidgets.QAction('Close', self)
        mode_menu.addAction(st_action)
        mode_menu.addAction(SR_action)
        mode_menu.addAction(Man_action)
        mode_menu.addAction(RESET_action)
        mode_menu.addAction(close_action)

        # use `connect` method to bind signals to desired behavior
        st_action.triggered.connect(self.St_page)
        SR_action.triggered.connect(self.SR_page)
        Man_action.triggered.connect(self.Man_page)
        RESET_action.triggered.connect(self.RESET_page)
        close_action.triggered.connect(self.close)

    def St_page(self):
        print("Capturing")

    def SR_page(self):
        print("Search&Receive Page")

    def Man_page(self):
        print("Manual Control Page")

    def RESET_page(self):
        print("RESET Page")


class SR(QtWidgets.QWidget):
    def __init__(self):
        super(SR, self).__init__()

        self.info_box("Deliver")
        self.choose_the_lock("Choose the locker")
        self.name_search("Receive")
        self.table_data("What's in the locker")


        layout =  QGridLayout()
        layout.addWidget(self.info_,0,0)
        layout.addWidget(self.choose_lock, 0, 1)
        layout.addWidget(self.nameGroup,1,0)
        layout.addWidget(self.table_, 1, 1)
        self.setLayout(layout)

    def name_search(self, title):
        self.nameGroup = QGroupBox(title)

        self.nameLabel = QLabel('Name/Address NO:')
        self.name_line = QLineEdit(self)
        self.name_line.setFixedSize(400,80)

        self.nlockLabel = QLabel('Locker NO:')
        self.nlock_line = QLineEdit(self)
        self.nlock_line.setFixedSize(400, 80)

        self.pybutton = QPushButton("Get the box", self)
        self.pybutton.setFixedSize(200,50)
        self.pybutton.clicked.connect(self.clickMethod)


        nameLayout = QGridLayout()
        nameLayout.setColumnStretch(2, 4)
        nameLayout.addWidget(self.nameLabel, 0, 0)
        nameLayout.addWidget(self.name_line, 0, 1)
        nameLayout.addWidget(self.nlockLabel, 1, 0)
        nameLayout.addWidget(self.nlock_line, 1, 1)
        nameLayout.addWidget(self.pybutton, 2, 1)

        self.nameGroup.setLayout(nameLayout)

    def clickMethod(self):
        print('Your name: ', self.name_line.text() )

    def info_box(self, title):
        self.info_ = QGroupBox(title)

        self.info_Label = QLabel('Name/Address NO:')
        self.info_line = QLineEdit("AAA")
        self.info_line.setFixedSize(400,80)
        self.info_button = QPushButton("Confirm", self)
        self.info_button.setFixedSize(200,50)
        self.info_button.clicked.connect(self.clickMethod2)


        infoLayout = QGridLayout()
        infoLayout.setColumnStretch(2, 4)
        infoLayout.addWidget(self.info_Label, 0, 0)
        infoLayout.addWidget(self.info_line, 0, 1)
        infoLayout.addWidget(self.info_button, 1, 1)

        self.info_.setLayout(infoLayout)

    def clickMethod2(self):
        print('Your name: ', self.info_line.text() )

    def choose_the_lock(self, title):
        self.choose_lock = QGroupBox(title)

        self.lock_buttonA = QPushButton("A", self)
        self.lock_buttonB = QPushButton("B", self)
        self.lock_buttonC = QPushButton("C", self)
        self.lock_buttonD = QPushButton("D", self)
        self.lock_buttonE = QPushButton("E", self)
        self.lock_buttonF = QPushButton("F", self)
        self.lock_buttonG = QPushButton("G", self)
        self.lock_buttonH = QPushButton("H", self)
        self.lock_buttonI = QPushButton("I", self)
        self.lock_buttonJ = QPushButton("J", self)
        self.lock_buttonK = QPushButton("K", self)
        self.lock_buttonL = QPushButton("L", self)
        self.lock_buttonM = QPushButton("M", self)
        self.lock_buttonN = QPushButton("N", self)

        self.lock_buttonA.setFixedSize(50, 40)
        self.lock_buttonB.setFixedSize(50, 40)
        self.lock_buttonC.setFixedSize(50, 40)
        self.lock_buttonD.setFixedSize(50, 40)
        self.lock_buttonE.setFixedSize(50, 40)
        self.lock_buttonF.setFixedSize(50, 40)
        self.lock_buttonG.setFixedSize(50, 40)
        self.lock_buttonH.setFixedSize(50, 40)
        self.lock_buttonI.setFixedSize(50, 40)
        self.lock_buttonJ.setFixedSize(50, 40)
        self.lock_buttonK.setFixedSize(50, 40)
        self.lock_buttonL.setFixedSize(50, 40)
        self.lock_buttonM.setFixedSize(50, 40)
        self.lock_buttonN.setFixedSize(50, 40)


        lockLayout = QGridLayout()
        lockLayout.setColumnStretch(2, 4)
        lockLayout.addWidget(self.lock_buttonA, 0, 0)
        lockLayout.addWidget(self.lock_buttonB, 1, 0)
        lockLayout.addWidget(self.lock_buttonC, 2, 0)
        lockLayout.addWidget(self.lock_buttonD, 0, 1)
        lockLayout.addWidget(self.lock_buttonE, 1, 1)
        lockLayout.addWidget(self.lock_buttonF, 2, 1)
        lockLayout.addWidget(self.lock_buttonG, 0, 2)
        lockLayout.addWidget(self.lock_buttonH, 1, 2)
        lockLayout.addWidget(self.lock_buttonI, 2, 2)
        lockLayout.addWidget(self.lock_buttonJ, 3, 2)
        lockLayout.addWidget(self.lock_buttonK, 0, 3)
        lockLayout.addWidget(self.lock_buttonL, 1, 3)
        lockLayout.addWidget(self.lock_buttonM, 2, 3)
        lockLayout.addWidget(self.lock_buttonN, 3, 3)


        self.choose_lock.setLayout(lockLayout)


    def table_data(self, title):
        self.table_ = QGroupBox(title)

        self.tableWidget = QTableWidget()
        self.tableWidget.setFixedSize(550,500)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("A"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("B"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("C"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("D"))
        self.tableWidget.setItem(4, 0, QTableWidgetItem("E"))
        self.tableWidget.setItem(5, 0, QTableWidgetItem("F"))
        self.tableWidget.setItem(6, 0, QTableWidgetItem("G"))
        self.tableWidget.setItem(7, 0, QTableWidgetItem("H"))
        self.tableWidget.setItem(8, 0, QTableWidgetItem("I"))
        self.tableWidget.setItem(9, 0, QTableWidgetItem("J"))
        self.tableWidget.setItem(10, 0, QTableWidgetItem("K"))
        self.tableWidget.setItem(11, 0, QTableWidgetItem("L"))
        self.tableWidget.setItem(12, 0, QTableWidgetItem("M"))
        self.tableWidget.setItem(13, 0, QTableWidgetItem("N"))

        self.tableWidget.setItem(0, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(2, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(3, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(4, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(5, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(6, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(7, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(8, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(9, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(10, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(11, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(12, 1, QTableWidgetItem(""))
        self.tableWidget.setItem(13, 1, QTableWidgetItem(""))

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

        tableLayout = QGridLayout()
        tableLayout.setColumnStretch(2, 4)
        tableLayout.addWidget(self.tableWidget, 0, 0)

        self.table_.setLayout(tableLayout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.setFont(QtGui.QFont("Courier New", 10))
    # creating main window
    mw = MainWindow()
    mw.resize(1200,800)
    mw.setWindowTitle("Module 8-9 | Group.7")
    mw.show()
    sys.exit(app.exec_())