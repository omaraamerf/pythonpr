from Datamanager import Datamanager
class Lecturer:
    def _init_(self, first_name, last_name, email, hire_date, department, lecturer_id=None):
        self.id = lecturer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.hire_date = hire_date
        self.department = department

    def save_to_db2(self, db_manager: Datamanager):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """INSERT INTO lecturers (first_name, last_name, email, hire_date, department)
            VALUES (?, ?, ?, ?, ?)""",
            (self.first_name, self.last_name, self.email, self.hire_date, self.department),
        )
        db_manager.conn.commit()

    @classmethod
    def get_all_lecturers(cls, db_manager: Datamanager):
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, email, hire_date, department FROM lecturers")
        result = cursor.fetchall()
        lecturers = []
        for row in result:
            lecturers.append(
                Lecturer(
                    lecturer_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    hire_date=row[4],
                    department=row[5],
                )
            )
        return lecturers

    def _str_(self):
        return f"Lecturer: {self.first_name} {self.last_name} (Email: {self.email}, Department: {self.department})"
    @classmethod
    def search_lecturers(cls, db_manager: Datamanager, search_query: str):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """SELECT id, first_name, last_name, email, hire_date, department
            FROM lecturers
            WHERE first_name LIKE ? OR last_name LIKE ? OR email LIKE ?""",
            (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"),
        )
        result = cursor.fetchall()
        lecturers = []
        for row in result:
            lecturers.append(
                Lecturer(
                    lecturer_id=row[0],
                    first_name=row[1],
                    last_name=row[2],
                    email=row[3],
                    hire_date=row[4],
                    department=row[5],
                )
            )
        return lecturers
    
    
    