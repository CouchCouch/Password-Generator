import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Password Generator")
    w.setGeometry(1200,1200,1200,150)

    password_length_label = QLabel(w)
    password_length_label.setText("Password Length:")
    password_length_label.move(50,20)

    password_length = QSpinBox(w)
    password_length.setMinimum(5)
    password_length.setValue(10)
    password_length.setMaximum(50)
    password_length.move(275,15)

    generate = QPushButton(w)
    generate.setText("Generate")
    generate.move(50,50)

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()