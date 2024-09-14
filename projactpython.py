from PyQt5 import QtCore , QtGui , QtWidgets  # noqa: F401
import sys

app = QtWidgets.QApplication(sys.argv)
Window = QtWidgets.QWidget()

# Window.setGeometry(100,100,800,600)
Window.resize(500, 500)
Window.move(400, 200)
Window.setWindowTitle("project ")
Window.setWindowIcon(QtGui.QIcon("C:\\Users\\zamzam\\Desktop\\project\\images\\th.jpeg"))
# Window.setStyleSheet('background-color: rgb(255,127,80);')

# button one 
button1 = QtWidgets.QPushButton('Add Student', Window)
button1.resize(150, 50)
button1.move(100, 20)
x = """
QPushButton {
    background-color: #3498db;
    color: white;
    border: 2px solid black;
    border-radius: 10px; 
    font-size: 16px;
    padding: 10px;

}
QPushButton:hover {
    
    background-color: qlineargradient(
        spread:pad, x1:0, y1:0, x2:1, y2:1,
        stop:0.7 #000000, stop:1 #3498db); 
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 16px;
    padding: 12px;
    transition: all 1s ease; 
}
"""

button1.setStyleSheet(x)
button1.setToolTip('add student')
# button1.clicked.conn(print("hello world"))

# button tow 
button2 = QtWidgets.QPushButton('remove Student', Window)
button2.resize(150, 50)
button2.move(250, 20)
# button2.clicked()

# windows exit button
exite = QtWidgets.QPushButton('remove Student', Window)
exite.resize(150, 50)
exite.move(150, 100)
exite.clicked.connect(exit)
exite.setIcon(QtGui.QIcon("C:\\Users\\zamzam\\Desktop\\project\\images\\logout.jpeg"))
exite.setStyleSheet("font-size:16px;")

# lable in window
label = QtWidgets.QLabel('Enter your name ', Window)
label.move(50, 300)
label.resize(150, 150)

# input 
textboex = QtWidgets.QLineEdit(Window)
textboex.move(75, 300)
textboex.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border: 2px solid #ddd;
                border-radius: 10px;
                font-size: 14px;
                background-color: #f4f4f9;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #007BFF;
                box-shadow: 0 0 8px rgba(0, 123, 255, 0.2);
            }
            QLineEdit:hover {
                border: 2px solid #0056b3; /* لون الحدود يصبح أغمق عند المرور بالماوس */
            }
        """)
Window.show()
app.exec_()



# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys

# app = QtWidgets.QApplication(sys.argv)
# homeinterface = QtWidgets.QWidget()

# # إعدادات النافذة
# homeinterface.resize(500, 300)
# homeinterface.move(400, 200)
# homeinterface.setWindowTitle("Project")
# homeinterface.setWindowIcon(QtGui.QIcon('C:\\Users\\zamzam\\Desktop\\project\\th.jpeg'))
# homeinterface.setStyleSheet("""
#     QWidget {
#         background-color: #f4f4f9;
#     }
# """)

# # إعداد التخطيط العمودي
# layout = QtWidgets.QVBoxLayout(homeinterface)
# layout.setContentsMargins(20, 20, 20, 20)
# layout.setSpacing(20)

# # زر "Add Student"
# button1 = QtWidgets.QPushButton('Add Student')
# button1.setStyleSheet("""
#     QPushButton {
#         padding: 15px 30px;
#         border: 2px solid transparent;
#         border-radius: 8px;
#         font-size: 18px;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         margin: 10px;
#         color: white;
#         font-weight: bold;
#         background-color: #4CAF50;
#     }
#     QPushButton:hover {
#         transform: scale(1.1);
#         border-color: white;
#     }
#     QPushButton:pressed {
#         background-color: #388E3C;
#     }
# """)
# button1.setToolTip('Add a new student')
# layout.addWidget(button1)

# # زر "Remove Student"
# button2 = QtWidgets.QPushButton('Remove Student')
# button2.setStyleSheet("""
#     QPushButton {
#         padding: 15px 30px;
#         border: 2px solid transparent;
#         border-radius: 8px;
#         font-size: 18px;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         margin: 10px;
#         color: white;
#         font-weight: bold;
#         background-color: #008CBA;
#     }
#     QPushButton:hover {
#         transform: scale(1.1);
#         border-color: white;
#     }
#     QPushButton:pressed {
#         background-color: #005f73;
#     }
# """)
# layout.addWidget(button2)

# # زر الخروج
# exit_button = QtWidgets.QPushButton('Exit')
# exit_button.setStyleSheet("""
#     QPushButton {
#         padding: 15px 30px;
#         border: 2px solid transparent;
#         border-radius: 8px;
#         font-size: 18px;
#         cursor: pointer;
#         transition: all 0.3s ease;
#         margin: 10px;
#         color: white;
#         font-weight: bold;
#         background-color: #f44336;
#     }
#     QPushButton:hover {
#         transform: scale(1.1);
#         border-color: white;
#     }
#     QPushButton:pressed {
#         background-color: #c62828;
#     }
# """)
# exit_button.setIcon(QtGui.QIcon("C:\\Users\\zamzam\\Desktop\\project\\logout.jpeg"))
# exit_button.clicked.connect(sys.exit)
# layout.addWidget(exit_button)

# homeinterface.show()
# app.exec_()
