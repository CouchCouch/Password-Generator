import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import password

def window():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Password Utilities")
    w.setGeometry(100,100,1000,500)

    # screen to choose the function

    choose = QLabel(w)
    choose.setText("Choose an option:")
    choose.resize(400,100)
    choose.move(400, 100)

    generate_password = QPushButton(w)
    generate_password.setText("Generate Password") 
    generate_password.resize(300,60)
    generate_password.move(195,190)

    decrypt_password = QPushButton(w)
    decrypt_password.setText("Decrypt Password")
    decrypt_password.resize(300,60)
    decrypt_password.move(505,190)

    add_password = QPushButton(w)
    add_password.setText("Add Password")
    add_password.resize(300,60)
    add_password.move(350,260)

    # screen shown to generate password

    GS_password_length_label = QLabel(w)
    GS_password_length_label.setText("Password Length:")
    GS_password_length_label.resize(110,40)
    GS_password_length_label.move(20,20)
    GS_password_length_label.hide()

    GS_password_length = QSpinBox(w)
    GS_password_length.setMinimum(5)
    GS_password_length.setValue(12)
    GS_password_length.setMaximum(50)
    GS_password_length.resize(100,40)
    GS_password_length.move(130,20)
    GS_password_length.hide()

    GS_generate = QPushButton(w)
    GS_generate.setText("Generate")
    GS_generate.resize(125,40)
    GS_generate.move(240,20)
    GS_generate.hide()

    GS_password_label = QLabel(w)
    GS_password_label.setText("Password:")
    GS_password_label.resize(130,40)
    GS_password_label.move(425,20)
    GS_password_label.hide()

    GS_password_out = QLineEdit(w)
    GS_password_out.setReadOnly(True)
    GS_password_out.setEchoMode(QLineEdit.Password)
    GS_password_out.resize(250,40)
    GS_password_out.move(495,20)
    GS_password_out.hide()

    GS_show_password_out = QPushButton(w)
    GS_show_password_out.setIcon(QIcon("icons/visibility.svg"))
    GS_show_password_out.move(750,20)
    GS_show_password_out.resize(40,40)
    GS_show_password_out.hide()

    GS_copy_password = QPushButton(w)
    GS_copy_password.setIcon(QIcon("icons/copy.svg"))
    GS_copy_password.resize(40,40)
    GS_copy_password.move(795,20)
    GS_copy_password.hide()

    GS_encrypt = QRadioButton(w)
    GS_encrypt.setText("Encrypt")
    GS_encrypt.resize(100,40)
    GS_encrypt.move(20,70)
    GS_encrypt.hide()

    # if encrypt is checked, show the following

    GS_encryption_password_label = QLabel(w)
    GS_encryption_password_label.setText("Encryption Password:")
    GS_encryption_password_label.resize(160,40)
    GS_encryption_password_label.move(125,70)
    GS_encryption_password_label.hide()

    GS_encryption_password = QLineEdit(w)
    GS_encryption_password.setEchoMode(QLineEdit.Password)
    GS_encryption_password.resize(230,40)
    GS_encryption_password.move(255,70)
    GS_encryption_password.hide()

    GS_account_name_label = QLabel(w)
    GS_account_name_label.setText("Account Name:")
    GS_account_name_label.resize(100,40)
    GS_account_name_label.move(500,70)
    GS_account_name_label.hide()

    GS_account_name = QLineEdit(w)
    GS_account_name.resize(230,40)
    GS_account_name.move(595,70)
    GS_account_name.hide()

    GS_encrypt_button = QPushButton(w)
    GS_encrypt_button.setText("Encrypt")
    GS_encrypt_button.resize(100,40)
    GS_encrypt_button.move(830,70)
    GS_encrypt_button.hide()

    # screen shown to decrypt password

    # screen shown to add password

    AS_password_label = QLabel(w)
    AS_password_label.setText("Password:")
    AS_password_label.resize(65,40)
    AS_password_label.move(20,20)
    AS_password_label.hide()

    AS_password_in = QLineEdit(w)
    AS_password_in.setEchoMode(QLineEdit.Password)
    AS_password_in.resize(735,40)
    AS_password_in.move(90,20)
    AS_password_in.hide()

    AS_encryption_password_label = QLabel(w)
    AS_encryption_password_label.setText("Encryption Password:")
    AS_encryption_password_label.resize(125,40)
    AS_encryption_password_label.move(20,70)
    AS_encryption_password_label.hide()

    AS_encryption_password = QLineEdit(w)
    AS_encryption_password.setEchoMode(QLineEdit.Password)
    AS_encryption_password.resize(230,40)
    AS_encryption_password.move(150,70)
    AS_encryption_password.hide()

    AS_account_name_label = QLabel(w)
    AS_account_name_label.setText("Account Name:")
    AS_account_name_label.resize(100,40)
    AS_account_name_label.move(390,70)
    AS_account_name_label.hide()

    AS_account_name = QLineEdit(w)
    AS_account_name.resize(230,40)
    AS_account_name.move(485,70)
    AS_account_name.hide()

    AS_encrypt_button = QPushButton(w)
    AS_encrypt_button.setText("Encrypt")
    AS_encrypt_button.resize(100,40)
    AS_encrypt_button.move(725,70)
    AS_encrypt_button.hide()


    # links the buttons to their functions

    generate_password.clicked.connect(lambda: generate_password_clicked())
    # decrypt_password.clicked.connect(lambda: decrypt_password_clicked())
    add_password.clicked.connect(lambda: add_password_clicked())
    GS_generate.clicked.connect(lambda: generate_clicked())
    GS_encrypt.clicked.connect(lambda: encrypt_clicked())
    GS_show_password_out.clicked.connect(lambda: show_password_out_clicked())
    GS_copy_password.clicked.connect(lambda: copy_password_clicked())

    def generate_password_clicked():
        """
        Hides the choose screen and shows the generate password screen
        """
        choose.hide()
        generate_password.hide()
        decrypt_password.hide()
        add_password.hide()
        GS_password_length_label.show()
        GS_password_length.show()
        GS_generate.show()
        GS_password_label.show()
        GS_password_out.show()
        GS_show_password_out.show()
        GS_encrypt.show()
        GS_copy_password.show()
    
    def encrypt_clicked():
        """
        Shows the encryption password and account name fields if encrypt is checked
        """
        if GS_encrypt.isChecked():
            GS_encryption_password_label.show()
            GS_encryption_password.show()
            GS_account_name_label.show()
            GS_account_name.show()
            GS_encrypt_button.show()
        else:
            GS_encryption_password_label.hide()
            GS_encryption_password.hide()
            GS_account_name_label.hide()
            GS_account_name.hide()
            GS_encrypt_button.hide()

    def generate_clicked():
        """
        Generates a password and shows it in the password field
        """
        GS_password_out.setText(password.generate(GS_password_length.value()))

    global showing
    showing = False

    def show_password_out_clicked():
        """
        Shows the password if the eye icon is clicked
        """
        global showing
        if showing:
            GS_show_password_out.setIcon(QIcon("icons/visibility.svg"))
            GS_password_out.setEchoMode(QLineEdit.Password)
            showing = False
        else:
            GS_show_password_out.setIcon(QIcon("icons/visibility_off.svg"))
            GS_password_out.setEchoMode(QLineEdit.Normal)
            showing = True
    
    def copy_password_clicked():
        """
        Copies the password to the clipboard
        """
        clipboard = QApplication.clipboard()
        clipboard.setText(GS_password_out.text())

    def add_password_clicked():
        """
        Hides the choose screen and shows the add password screen
        """
        choose.hide()
        generate_password.hide()
        decrypt_password.hide()
        add_password.hide()
        AS_password_label.show()
        AS_password_in.show()
        AS_encryption_password_label.show()
        AS_encryption_password.show()
        AS_account_name_label.show()
        AS_account_name.show()
        AS_encrypt_button.show()
    
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()