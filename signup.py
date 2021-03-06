# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MyUi_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(813, 540)
        Dialog.setStyleSheet("background-color: rgb(14, 32, 40);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 250, 60, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        #self.u_name_label = QtWidgets.QLabel(Dialog)
        #self.u_name_label.setGeometry(QtCore.QRect(230, 230, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        #self.u_name_label.setFont(font)
        #self.u_name_label.setStyleSheet("color: rgb(231, 236, 247);")
        #self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.u_name_label.setObjectName("u_name_label")
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(380, 290, 181, 21))
        self.uname_lineEdit.setStyleSheet("background-color: rgb(240, 251, 239);")
        self.uname_lineEdit.setInputMask("")
        self.uname_lineEdit.setText("")
        self.uname_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.u_name_label_2 = QtWidgets.QLabel(Dialog)
        self.u_name_label_2.setGeometry(QtCore.QRect(260, 290, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.u_name_label_2.setFont(font)
        self.u_name_label_2.setStyleSheet("color: rgb(231, 236, 247);")
        self.u_name_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.u_name_label_2.setObjectName("u_name_label_2")
        #self.email_lineEdit = QtWidgets.QLineEdit(Dialog)
        #self.email_lineEdit.setGeometry(QtCore.QRect(380, 230, 181, 21))
        #self.email_lineEdit.setStyleSheet("background-color: rgb(240, 251, 239);")
        #self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.password_lineEdit.setGeometry(QtCore.QRect(380, 350, 181, 21))
        self.password_lineEdit.setStyleSheet("background-color: rgb(240, 251, 239);")
        self.password_lineEdit.setInputMask("")
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.pass_label_2 = QtWidgets.QLabel(Dialog)
        self.pass_label_2.setGeometry(QtCore.QRect(230, 350, 131, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pass_label_2.setFont(font)
        self.pass_label_2.setStyleSheet("color: rgb(231, 236, 247);")
        self.pass_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label_2.setObjectName("pass_label_2")
        self.signup_btn = QtWidgets.QPushButton(Dialog)
        self.signup_btn.setGeometry(QtCore.QRect(310, 430, 171, 31))
        self.signup_btn.setStyleSheet("QPushButton#signup_btn{\n"
"background-color:rgba(2,65,118,255);\n"
"background-color:rgba(255,255,255,200);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#signup_btn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgb(255, 255, 255);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#signup_btn:hover{\n"
"background-color:rgb(255, 255, 255);}")
        self.signup_btn.setObjectName("signup_btn")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 40, 171, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../Downloads/WhatsApp Image 2021-06-20 at 2.56.01 PM (1).jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        #self.u_name_label.setText(_translate("Dialog", "Your Email Address"))
        self.u_name_label_2.setText(_translate("Dialog", "Username"))
        self.pass_label_2.setText(_translate("Dialog", "Create a Password"))
        self.signup_btn.setText(_translate("Dialog", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
