import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class TeacherApp(QWidget):
    def __init__(self):
        super().__init__()

        # إعداد الواجهة
        self.setWindowTitle("إدارة المعلمين")
        self.setGeometry(100, 100, 800, 600)

        # إعداد الخلفية
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("images/download.jpeg"))
        self.background_label.setScaledContents(True)  # جعل الصورة تتناسب مع حجم الواجهة

        # إنشاء مربع البحث
        self.search_label = QLabel("بحث عن معلم (بالإيميل أو الاسم):")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("أدخل البريد الإلكتروني أو الاسم")
        self.search_input.setFixedWidth(int(self.width() * 0.50))  # ضبط العرض ليكون 50% من العرض
        self.search_input.setFixedHeight(30)  # تقليل الارتفاع
        self.search_input.setStyleSheet("margin-left: 0px;")  # وضعه على أقصى اليسار

        # زر إضافة معلم
        self.add_teacher_button = QPushButton("إضافة معلم")
        self.add_teacher_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 12px;
                padding: 8px;
                border-radius: 10px;
                width: 150px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        # إنشاء جدول لعرض بيانات المعلم
        self.teacher_table = QTableWidget()
        self.teacher_table.setColumnCount(4)  # اسم، إيميل، زر إضافة وظيفة، زر حذف معلم
        self.teacher_table.setHorizontalHeaderLabels(["الاسم", "الإيميل", "إضافة وظيفة", "حذف معلم"])
        self.teacher_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # ضبط الجدول لعرض 6 صفوف فقط مع إمكانية التمرير
        self.teacher_table.setFixedHeight(180)
        self.teacher_table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # ملء الجدول ببيانات افتراضية
        for i in range(10):
            self.add_teacher_row(f"معلم {i+1}", f"teacher{i+1}@school.com")

        # تصميم التخطيط
        layout = QVBoxLayout(self)
        search_layout = QHBoxLayout()

        # إضافة مسافة من الأعلى
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # إضافة العناصر بتنسيق مع الحواف
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.add_teacher_button)
        
        layout.addLayout(search_layout)
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))  # إضافة فراغ
        layout.addWidget(self.teacher_table)

        self.setLayout(layout)

    def resizeEvent(self, event):
        # ضبط حجم الخلفية عند تغيير حجم النافذة
        self.background_label.resize(self.size())
        super().resizeEvent(event)

    def add_teacher_row(self, name, email):
        row_position = self.teacher_table.rowCount()
        self.teacher_table.insertRow(row_position)

        # إضافة بيانات المعلم
        self.teacher_table.setItem(row_position, 0, QTableWidgetItem(name))
        self.teacher_table.setItem(row_position, 1, QTableWidgetItem(email))

        # زر إضافة وظيفة
        add_job_button = QPushButton("إضافة واجب")
        add_job_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 10px;
                padding: 4px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.teacher_table.setCellWidget(row_position, 2, add_job_button)

        # زر حذف معلم مع أيقونة
        delete_teacher_button = QPushButton()
        delete_teacher_button.setIcon(QIcon("delete_icon.png"))  # إضافة الأيقونة
        delete_teacher_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                padding: 4px;
                border-radius: 8px;
                width: 50px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.teacher_table.setCellWidget(row_position, 3, delete_teacher_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # إنشاء الواجهة
    window = TeacherApp()
    window.show()

    sys.exit(app.exec_())
