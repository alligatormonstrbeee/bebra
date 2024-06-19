import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from chek_bd import *
from des import *

class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.chek_bd = CheckThread()
        self.chek_bd.mysignal.connect(self.signal_handler)



    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper#

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)




    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.chek_bd.thr_login(name,passw)

    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.chek_bd.thr_register(name,passw)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())