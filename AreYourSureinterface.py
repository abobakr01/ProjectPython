import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt

class AreYouSureInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # إعداد حجم النافذة والعنوان
        self.setWindowTitle('Confirmation Page')
        self.setGeometry(100, 100, 400, 300)

        # إعداد الخلفية باستخدام صورة مع ملء الصورة ابتداءً من المنتصف
        background_image = QPixmap('images\download.jpeg')
        background_image = background_image.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)

        # إعداد الحاوية الشفافة داخل النافذة
        container = QWidget(self)
        container.setStyleSheet("background-color: rgba(255, 255, 255, 0.3); border-radius: 15px;")
        container.setFixedSize(300, 200)

        # إعداد النص داخل الحاوية
        label = QLabel('هل أنت متأكد من عملية الحذف؟', container)
        label.setStyleSheet("font-size: 16px; color: #343a40;")
        label.setAlignment(Qt.AlignCenter)

        # إعداد الأزرار مع انحناء الزوايا
        yes_button = QPushButton('نعم', container)
        yes_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 15px;  /* زيادة الانحناء */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        yes_button.clicked.connect(self.confirm_action)

        no_button = QPushButton('لا', container)
        no_button.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border-radius: 15px;  /* زيادة الانحناء */
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        no_button.clicked.connect(self.reject_action)

        # ترتيب الأزرار بجانب بعضها البعض
        button_layout = QHBoxLayout()
        button_layout.addWidget(yes_button)
        button_layout.addWidget(no_button)

        # ترتيب جميع العناصر داخل الحاوية
        layout = QVBoxLayout(container)
        layout.addWidget(label)
        layout.addLayout(button_layout)
        layout.setAlignment(Qt.AlignCenter)

        # ضبط موضع الحاوية في منتصف النافذة
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(container)
        main_layout.setAlignment(Qt.AlignCenter)

    def confirm_action(self):
        QMessageBox.information(self, 'تم التأكيد', 'تم تأكيد عملية الحذف.')

    def reject_action(self):
        QMessageBox.information(self, 'تم الإلغاء', 'تم إلغاء عملية الحذف.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AreYouSureInterface()
    window.show()
    sys.exit(app.exec_())
