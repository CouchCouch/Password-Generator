import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import password

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Password Utilities")
    w.setGeometry(100,100,900,500)

    choose = QLabel(w)
    choose.setText("Choose an option:")
    choose.resize(400,100)
    choose.move(350, 100)

    generate_password = QPushButton(w)
    generate_password.setText("Generate Password") 
    generate_password.resize(300,60)
    generate_password.move(145,190)

    decrypt_password = QPushButton(w)
    decrypt_password.setText("Decrypt Password")
    decrypt_password.resize(300,60)
    decrypt_password.move(455,190)

    add_password = QPushButton(w)
    add_password.setText("Add Password")
    add_password.resize(300,60)
    add_password.move(300,260)

    password_length_label = QLabel(w)
    password_length_label.setText("Password Length:")
    password_length_label.resize(230,40)
    password_length_label.move(20,20)
    password_length_label.hide()

    password_length = QSpinBox(w)
    password_length.setMinimum(5)
    password_length.setValue(10)
    password_length.setMaximum(50)
    password_length.resize(100,40)
    password_length.move(250,20)
    password_length.hide()

    generate = QPushButton(w)
    generate.setText("Generate")
    generate.resize(125,40)
    generate.move(360,20)
    generate.hide()

    password_label = QLabel(w)
    password_label.setText("Password:")
    password_label.resize(130,40)
    password_label.move(495,20)
    password_label.hide()

    password = QLineEdit(w)
    password.setReadOnly(True)
    password.move(630,20)
    password.resize(230,40)
    password.hide()
    
    encrypt = QRadioButton(w)
    encrypt.setText("Encrypt")
    encrypt.move(20,70)
    encrypt.resize(140,40)
    encrypt.hide()

    encryption_password_label = QLabel(w)
    encryption_password_label.setText("Encryption Password:")
    encryption_password_label.resize(260,40)
    encryption_password_label.move(165,70)
    encryption_password_label.hide()

    encryption_password = QLineEdit(w)
    encryption_password.setEchoMode(QLineEdit.Password)
    encryption_password.move(430,70)
    encryption_password.resize(230,40)
    encryption_password.hide()

    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()