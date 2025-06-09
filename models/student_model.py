from datetime import datetime

class Student:
    def __init__(self, name, email, phone=None, course=None, year=None, join_date=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.course = course
        self.year = year
        self.join_date = join_date or datetime.now().date()
    
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'course': self.course,
            'year': self.year,
            'join_date': str(self.join_date)
        }