from Datamanager import Datamanager

class Grade:
    def _init_(self, grade_value, assignment_id, student_id, grade_id=None):
        self.id = grade_id
        self.grade_value = grade_value
        self.assignment_id = assignment_id
        self.student_id = student_id

    def save_to_db3(self, db_manager: Datamanager):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """INSERT INTO grades (grade, assignment_id, student_id)
            VALUES (?, ?, ?)""",
            (self.grade_value, self.assignment_id, self.student_id),
        )
        db_manager.conn.commit()

    @classmethod
    def get_all_grades(cls, db_manager: Datamanager):
        cursor = db_manager.conn.cursor()
        cursor.execute("SELECT id, grade, assignment_id, student_id FROM grades")
        result = cursor.fetchall()
        grades = []
        for row in result:
            grades.append(
                Grade(
                    grade_id=row[0],
                    grade_value=row[1],
                    assignment_id=row[2],
                    student_id=row[3],
                )
            )
        return grades

    def _str_(self):
        return f"Grade: {self.grade_value} (Assignment ID: {self.assignment_id}, Student ID: {self.student_id})"
    @classmethod
    def get_grades_by_assignment(cls, db_manager: Datamanager, assignment_id: int):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """SELECT id, grade, assignment_id, student_id 
            FROM grades 
            WHERE assignment_id = ?""",
            (assignment_id,),
        )
        result = cursor.fetchall()
        grades = []
        for row in result:
            grades.append(
                Grade(
                    grade_id=row[0],
                    grade_value=row[1],
                    assignment_id=row[2],
                    student_id=row[3],
                )
            )
        return grades
    def update_grade(self, db_manager: Datamanager, new_grade_value: float):
        cursor = db_manager.conn.cursor()
        cursor.execute(
            """UPDATE grades
            SET grade = ?
            WHERE assignment_id = ? AND student_id = ?""",
            (new_grade_value, self.assignment_id, self.student_id),
        )
        db_manager.conn.commit()