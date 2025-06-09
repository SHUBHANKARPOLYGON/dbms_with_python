import re
from datetime import datetime

class InputValidator:
    @staticmethod
    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_phone(phone):
        if not phone:
            return True
        pattern = r'^\+?[0-9\s-]{10,15}$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def validate_date(date_str):
        if not date_str:
            return True
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    @staticmethod
    def validate_year(year):
        if not year:
            return True
        try:
            year_int = int(year)
            return 1 <= year_int <= 5
        except ValueError:
            return False