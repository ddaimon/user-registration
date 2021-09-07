import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Giris(QDialog):
    def __init__(self):
        super(Giris,self).__init__()
        loadUi("giris.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)


    def loginfunction(self):
        email = self.email.text()
        sifre = self.sifre.text()
        print("Basariyla email:",email, "ve sifreyle giris yapildi:",sifre)

    def gotocreate(self):
        createacc = Kayit()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Kayit(QDialog):
    def __init__(self):
        super(Kayit,self).__init__()
        loadUi("kayıt.ui",self)
        self.signupbutton.clicked.connect(self.kayitfunction)
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)


    def kayitfunction(self):
        email = self.email.text()
        if self.sifre.text()==self.confirmpass.text():
            sifre = self.sifre.text()
            print("Basariyla email:",email, "ve sifreyle kayıt oldunuz:",sifre)
            giris = Giris()
            widget.addWidget(giris)
            widget.setCurrentIndex(widget.setCurrentIndex() + 1)




app = QApplication(sys.argv)
mainwindow = Giris()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(480)
widget.show()
app.exec()