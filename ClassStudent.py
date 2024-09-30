
class Student:
    def __init__(self, id , firstName , lastName , email , dateOfBirth , dateOfEnroll):
        self.id = id
        self.firstName=firstName
        self.lastName-lastName
        self.email=email
        self.dateOfBirth=dateOfBirth
        self.dateOFEnroll=dateOfEnroll
    




# import sqlite3
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

# # 1. إعداد قاعدة البيانات باستخدام SQLite
# def setup_database():
#     conn = sqlite3.connect('students_grades.db')
#     cursor = conn.cursor()

#     # إنشاء جدول الطلاب
    # cursor.execute('''
    # CREATE TABLE IF NOT EXISTS students (
    #     student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT NOT NULL,
    #     email TEXT UNIQUE
    # )
    # ''')

#     # إنشاء جدول المواد الدراسية
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS courses (
#         course_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         course_name TEXT NOT NULL
#     )
#     ''')

#     # إنشاء جدول الدرجات
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS grades (
#         grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         student_id INTEGER,
#         course_id INTEGER,
#         grade REAL,
#         FOREIGN KEY(student_id) REFERENCES students(student_id),
#         FOREIGN KEY(course_id) REFERENCES courses(course_id)
#     )
#     ''')

#     conn.commit()
#     return conn, cursor

# conn, cursor = setup_database()

# # 2. وظائف التعامل مع قاعدة البيانات
# # إضافة طالب
# def add_student(name, email):
#     cursor.execute('INSERT INTO students (name, email) VALUES (?, ?)', (name, email))
#     conn.commit()

# # إضافة مادة دراسية
# def add_course(course_name):
#     cursor.execute('INSERT INTO courses (course_name) VALUES (?)', (course_name,))
#     conn.commit()

# # إضافة درجة لطالب
# def add_grade(student_id, course_id, grade):
#     cursor.execute('INSERT INTO grades (student_id, course_id, grade) VALUES (?, ?, ?)', (student_id, course_id, grade))
#     conn.commit()

# # استرجاع درجات طالب
# def get_student_grades(student_id):
#     cursor.execute('''
#     SELECT courses.course_name, grades.grade FROM grades 
#     JOIN courses ON grades.course_id = courses.course_id 
#     WHERE grades.student_id = ?
#     ''', (student_id,))
#     return cursor.fetchall()

# # تحديث درجة لطالب
# def update_grade(student_id, course_id, new_grade):
#     cursor.execute('''
#     UPDATE grades
#     SET grade = ?
#     WHERE student_id = ? AND course_id = ?
#     ''', (new_grade, student_id, course_id))
#     conn.commit()

# # حذف طالب
# def delete_student(student_id):
#     cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
#     conn.commit()

# # حذف مادة دراسية
# def delete_course(course_id):
#     cursor.execute('DELETE FROM courses WHERE course_id = ?', (course_id,))
#     conn.commit()
# def Select_course(course_id):
#     cursor.execute('SELECT * FROM courses WHERE course_id = ?', (course_id,))
#     return cursor.fetchone()
# # 3. الواجهات الرسومية باستخدام PyQt5
# # واجهة إضافة طالب
# class AddStudentWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('إضافة طالب')
#         self.setGeometry(300, 300, 300, 200)
        
#         layout = QVBoxLayout()

#         self.name_label = QLabel('اسم الطالب:')
#         self.name_input = QLineEdit()
#         self.email_label = QLabel('البريد الإلكتروني:')
#         self.email_input = QLineEdit()

#         self.add_button = QPushButton('إضافة طالب')
#         self.add_button.clicked.connect(self.add_student)

#         layout.addWidget(self.name_label)
#         layout.addWidget(self.name_input)
#         layout.addWidget(self.email_label)
#         layout.addWidget(self.email_input)
#         layout.addWidget(self.add_button)

#         self.setLayout(layout)

#     def add_student(self):
#         name = self.name_input.text()
#         email = self.email_input.text()
#         add_student(name, email)  # إضافة الطالب لقاعدة البيانات

# # واجهة إضافة مادة دراسية
# class AddCourseWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('إضافة مادة دراسية')
#         self.setGeometry(300, 300, 300, 200)
        
#         layout = QVBoxLayout()

#         self.course_label = QLabel('اسم المادة الدراسية:')
#         self.course_input = QLineEdit()

#         self.add_button = QPushButton('إضافة مادة دراسية')
#         self.add_button.clicked.connect(self.add_course)

#         layout.addWidget(self.course_label)
#         layout.addWidget(self.course_input)
#         layout.addWidget(self.add_button)

#         self.setLayout(layout)

#     def add_course(self):
#         course_name = self.course_input.text()
#         add_course(course_name)  # إضافة المادة لقاعدة البيانات

# # واجهة إضافة درجة لطالب
# class AddGradeWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('إضافة درجة')
#         self.setGeometry(300, 300, 300, 200)
        
#         layout = QVBoxLayout()

#         self.student_id_label = QLabel('رقم الطالب:')
#         self.student_id_input = QLineEdit()
#         self.course_id_label = QLabel('رقم المادة:')
#         self.course_id_input = QLineEdit()
#         self.grade_label = QLabel('الدرجة:')
#         self.grade_input = QLineEdit()

#         self.add_button = QPushButton('إضافة درجة')
#         self.add_button.clicked.connect(self.add_grade)

#         layout.addWidget(self.student_id_label)
#         layout.addWidget(self.student_id_input)
#         layout.addWidget(self.course_id_label)
#         layout.addWidget(self.course_id_input)
#         layout.addWidget(self.grade_label)
#         layout.addWidget(self.grade_input)
#         layout.addWidget(self.add_button)

#         self.setLayout(layout)

#     def add_grade(self):
#         student_id = int(self.student_id_input.text())
#         course_id = int(self.course_id_input.text())
#         grade = float(self.grade_input.text())
#         add_grade(student_id, course_id, grade)  # إضافة الدرجة لقاعدة البيانات

# # 4. تشغيل التطبيق
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)

#     # نوافذ التطبيق
#     student_window = AddStudentWindow()
#     course_window = AddCourseWindow()
#     grade_window = AddGradeWindow()

#     # عرض واجهة إضافة الطالب
#     student_window.show()
#     course_window.show()
#     grade_window.show()

#     sys.exit(app.exec_())
# print(Select_course())
# print("hello")
