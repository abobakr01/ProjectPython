from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

# إعداد النافذة
homeinterface = QtWidgets.QWidget()
homeinterface.resize(800, 600)
homeinterface.move(400, 200)
homeinterface.setWindowTitle("Project")
homeinterface.setWindowIcon(QtGui.QIcon('C:\\Users\\zamzam\\Desktop\\project\\images\\th.jpeg'))

# إعداد خلفية الصورة للواجهة
background_pixmap = QtGui.QPixmap('C:/Users/zamzam/Desktop/project/images/download.jpeg')
background_label = QtWidgets.QLabel(homeinterface)
background_label.setPixmap(background_pixmap)
background_label.setScaledContents(True)
background_label.setGeometry(homeinterface.rect())  # ملء الواجهة بالكامل

# إعداد تخطيط عمودي للأزرار مع المحاذاة في المنتصف
button_layout = QtWidgets.QVBoxLayout()
button_layout.setContentsMargins(20, 20, 20, 20)
button_layout.setSpacing(20)
button_layout.setAlignment(QtCore.Qt.AlignCenter)

# زر "Add Student"
button1 = QtWidgets.QPushButton('Add Student')
button1.setStyleSheet("""
    QPushButton {
        padding: 15px 30px;
        border: 2px solid transparent;
        border-radius: 8px;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 10px;
        color: white;
        font-weight: bold;
        background-color: #4CAF50;
    }
    QPushButton:hover {
        transform: scale(1.1);
        border-color: white;
    }
    QPushButton:pressed {
        background-color: #388E3C;
    }
""")
button1.setToolTip('Add a new student')
button_layout.addWidget(button1)

# زر "Remove Student"
button2 = QtWidgets.QPushButton('Remove Student')
button2.setStyleSheet("""
    QPushButton {
        padding: 15px 30px;
        border: 2px solid transparent;
        border-radius: 8px;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 10px;
        color: white;
        font-weight: bold;
        background-color: #008CBA;
    }
    QPushButton:hover {
        transform: scale(1.1);
        border-color: white;
    }
    QPushButton:pressed {
        background-color: #005f73;
    }
""")
button_layout.addWidget(button2)

# زر الخروج
exit_button = QtWidgets.QPushButton('Exit')
exit_button.setStyleSheet("""
    QPushButton {
        padding: 15px 30px;
        border: 2px solid transparent;
        border-radius: 8px;
        font-size: 18px;
        cursor: pointer;
        transition: all 0.3s ease;
        margin: 10px;
        color: white;
        font-weight: bold;
        background-color: #f44336;
    }
    QPushButton:hover {
        transform: scale(1.1);
        border-color: white;
    }
    QPushButton:pressed {
        background-color: #c62828;
    }
""")
exit_button.setIcon(QtGui.QIcon("C:/Users/zamzam/Desktop/project/images/logout.jpeg"))
exit_button.setIconSize(QtCore.QSize(20, 20))  # ضبط حجم الأيقونة
exit_button.clicked.connect(sys.exit)
button_layout.addWidget(exit_button)

# إعداد تخطيط رئيسي للواجهة
main_layout = QtWidgets.QVBoxLayout(homeinterface)
main_layout.addStretch()  # لضمان أن الأزرار تكون في منتصف الشاشة
main_layout.addLayout(button_layout)
main_layout.addStretch()  # لضمان أن الأزرار تكون في منتصف الشاشة

homeinterface.setLayout(main_layout)

def resizeEvent(event):
    # تحديث خلفية الصورة عند تغيير حجم النافذة
    background_label.setGeometry(homeinterface.rect())
    QtWidgets.QWidget.resizeEvent(homeinterface, event)

homeinterface.resizeEvent = resizeEvent

homeinterface.show()
sys.exit(app.exec_())
