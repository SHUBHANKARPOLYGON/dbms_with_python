import pandas as pd
from services.database_service import DatabaseService

class ExportService:
    @staticmethod
    def export_to_excel(filename='exports/students_data.xlsx'):
        db_service = DatabaseService()
        students = db_service.get_all_students()
        
        # Create DataFrame
        df = pd.DataFrame(students, columns=[
            'id', 'name', 'email', 'phone', 'course', 'year', 'join_date'
        ])
        
        # Export to Excel
        df.to_excel(filename, index=False)
        return filename