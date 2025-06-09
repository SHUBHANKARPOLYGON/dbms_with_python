import sqlite3
from datetime import datetime
from models.student_model import Student

class DatabaseService:
    def __init__(self, db_name='database/student_management.db'):
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    phone TEXT,
                    course TEXT,
                    year INTEGER,
                    join_date DATE
                )
            ''')
            conn.commit()
    
    def _get_connection(self):
        return sqlite3.connect(self.db_name)
    
    def add_student(self, student):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (name, email, phone, course, year, join_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                student.name,
                student.email,
                student.phone,
                student.course,
                student.year,
                student.join_date
            ))
            conn.commit()
    
    def get_all_students(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students')
            return cursor.fetchall()
    
    def update_student(self, student_id, updated_student):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE students
                SET name=?, email=?, phone=?, course=?, year=?, join_date=?
                WHERE id=?
            ''', (
                updated_student.name,
                updated_student.email,
                updated_student.phone,
                updated_student.course,
                updated_student.year,
                updated_student.join_date,
                student_id
            ))
            conn.commit()
    
    def delete_student(self, student_id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
            conn.commit()
    
    def search_students(self, search_term):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM students
                WHERE name LIKE ? OR email LIKE ? OR course LIKE ?
            ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
            return cursor.fetchall()