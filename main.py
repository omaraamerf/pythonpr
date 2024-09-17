from Datamanager import Datamanager
from Lecturer import Lecturer
from Grades import Grade
from assignments import Assignment
from datetime import date
from Student import Student

def main():
    db_manager = Datamanager()
    # student = Student("third_name", "last_name", "example@example.com", 2002)  # Create a Student object
    # student.save_to_db(db_manager)
    print("Done")
    
    print("hh\n")
    result=Student.search_students_by_dob(db_manager,"1995", "2005" )
    print(result)
    # Print the results
    for student in result:
        print(f"Name: {student.first_name} {student.last_name}, DOB: {student.date_of_birth}")
    print("jjjj")
    
    db_manager.close()
if __name__ == "__main__":
    main()