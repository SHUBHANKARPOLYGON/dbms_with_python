from services.database_service import DatabaseService
from services.export_service import ExportService
from models.student_model import Student
from utils.input_validation import InputValidator
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Students")
    print("6. Export to Excel")
    print("7. Exit")

def add_student(db_service):
    print("\nAdd New Student")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    
    if not InputValidator.validate_email(email):
        print("Invalid email format!")
        return
    
    phone = input("Phone (optional): ").strip() or None
    if phone and not InputValidator.validate_phone(phone):
        print("Invalid phone number format!")
        return
    
    course = input("Course (optional): ").strip() or None
    year = input("Year (1-5, optional): ").strip() or None
    if year and not InputValidator.validate_year(year):
        print("Year must be between 1 and 5!")
        return
    
    join_date = input("Join date (YYYY-MM-DD, optional): ").strip() or None
    if join_date and not InputValidator.validate_date(join_date):
        print("Invalid date format! Use YYYY-MM-DD")
        return
    
    student = Student(name, email, phone, course, year, join_date)
    db_service.add_student(student)
    print("Student added successfully!")

def view_students(db_service):
    students = db_service.get_all_students()
    if not students:
        print("No students found!")
        return
    
    print("\nStudent List:")
    print("-" * 80)
    print(f"{'ID':<5}{'Name':<20}{'Email':<25}{'Course':<15}{'Year':<5}")
    print("-" * 80)
    for student in students:
        print(f"{student[0]:<5}{student[1]:<20}{student[2]:<25}{student[4] or 'N/A':<15}{student[5] or 'N/A':<5}")

def update_student(db_service):
    student_id = input("Enter student ID to update: ")
    try:
        student_id = int(student_id)
    except ValueError:
        print("Invalid student ID!")
        return
    
    # Get existing student data
    students = db_service.get_all_students()
    student_to_update = next((s for s in students if s[0] == student_id), None)
    
    if not student_to_update:
        print("Student not found!")
        return
    
    print("\nCurrent Student Data:")
    print(f"1. Name: {student_to_update[1]}")
    print(f"2. Email: {student_to_update[2]}")
    print(f"3. Phone: {student_to_update[3]}")
    print(f"4. Course: {student_to_update[4]}")
    print(f"5. Year: {student_to_update[5]}")
    print(f"6. Join Date: {student_to_update[6]}")
    
    # Get updated values
    name = input(f"Enter new name (current: {student_to_update[1]}): ").strip() or student_to_update[1]
    email = input(f"Enter new email (current: {student_to_update[2]}): ").strip() or student_to_update[2]
    
    if not InputValidator.validate_email(email):
        print("Invalid email format!")
        return
    
    phone = input(f"Enter new phone (current: {student_to_update[3]}): ").strip() or student_to_update[3]
    if phone and not InputValidator.validate_phone(phone):
        print("Invalid phone number format!")
        return
    
    course = input(f"Enter new course (current: {student_to_update[4]}): ").strip() or student_to_update[4]
    year = input(f"Enter new year (current: {student_to_update[5]}): ").strip() or student_to_update[5]
    if year and not InputValidator.validate_year(year):
        print("Year must be between 1 and 5!")
        return
    
    join_date = input(f"Enter new join date (current: {student_to_update[6]}): ").strip() or student_to_update[6]
    if join_date and not InputValidator.validate_date(join_date):
        print("Invalid date format! Use YYYY-MM-DD")
        return
    
    updated_student = Student(name, email, phone, course, year, join_date)
    db_service.update_student(student_id, updated_student)
    print("Student updated successfully!")

def delete_student(db_service):
    student_id = input("Enter student ID to delete: ")
    try:
        student_id = int(student_id)
    except ValueError:
        print("Invalid student ID!")
        return
    
    confirm = input(f"Are you sure you want to delete student with ID {student_id}? (y/n): ").lower()
    if confirm == 'y':
        db_service.delete_student(student_id)
        print("Student deleted successfully!")

def search_students(db_service):
    search_term = input("Enter search term: ").strip()
    students = db_service.search_students(search_term)
    
    if not students:
        print("No matching students found!")
        return
    
    print("\nSearch Results:")
    print("-" * 80)
    print(f"{'ID':<5}{'Name':<20}{'Email':<25}{'Course':<15}{'Year':<5}")
    print("-" * 80)
    for student in students:
        print(f"{student[0]:<5}{student[1]:<20}{student[2]:<25}{student[4] or 'N/A':<15}{student[5] or 'N/A':<5}")

def export_data():
    try:
        filename = ExportService.export_to_excel()
        print(f"Data exported successfully to {filename}")
    except Exception as e:
        print(f"Error exporting data: {str(e)}")

def main():
    db_service = DatabaseService()
    
    # Create necessary directories
    os.makedirs('database', exist_ok=True)
    os.makedirs('exports', exist_ok=True)
    
    while True:
        clear_screen()
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            add_student(db_service)
        elif choice == '2':
            view_students(db_service)
        elif choice == '3':
            update_student(db_service)
        elif choice == '4':
            delete_student(db_service)
        elif choice == '5':
            search_students(db_service)
        elif choice == '6':
            export_data()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()