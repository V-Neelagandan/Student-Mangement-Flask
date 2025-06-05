
import sqlite3
from flask import request, make_response

connection_string = sqlite3.connect('College.db', check_same_thread=False)
connection_string.row_factory = sqlite3.Row
quary = connection_string.cursor()

class Student:
    def get_student_data(self):
        try:
            quary.execute("SELECT * FROM student")
            Student_data = [dict(data) for data in quary.fetchall()]
            return make_response({"success": "Data retrieved successfully", "Student_data": Student_data}, 200)
        except Exception as e:
            return make_response({"error": f"Something went wrong: {e}"}, 400)

    def post_student_data(self, data):
        try:
            quary.execute(
                'INSERT INTO student(Student_Name, Student_Age, Student_Contact_Email, Student_Contact_Number) VALUES (?, ?, ?, ?)',
                (data["Student_Name"], data["Student_Age"], data["Student_Contact_Email"], data["Student_Contact_Number"])
            )
            connection_string.commit()
            return make_response({"success": "Student Data added successfully!"}, 200)
        except Exception as e:
            return make_response({"error": f"Something went wrong: {e}"}, 400)

    def delete_student_data(self, id):
        try:
            quary.execute("DELETE FROM student WHERE Id = ?", (id,))
            connection_string.commit()
            return make_response({"success": "Student data deleted successfully"}, 200)
        except Exception as e:
            return make_response({"error": f"Something went wrong: {e}"}, 400)

    def update_student_data(self, id, data):
        try:
            quary.execute(
                "UPDATE student SET Student_Name = ?, Student_Age = ?, Student_Contact_Email = ?, Student_Contact_Number = ? WHERE Id = ?",
                (data["Student_Name"], data["Student_Age"], data["Student_Contact_Email"], data["Student_Contact_Number"], id)
            )
            connection_string.commit()
            return make_response({"success": "Student data updated successfully"}, 200)
        except Exception as e:
            return make_response({"error": f"Something went wrong: {e}"}, 400)

    def get_Student_data_By_id(self, id):
        try:
            quary.execute("SELECT * FROM student WHERE Id = ?", (id,))
            student_data = [dict(records) for records in quary.fetchall()]
            if not student_data:
                return make_response({"error": f"Student with ID {id} not found"}, 404)
            return make_response({"success": "Data retrieved successfully", "Student_Data": student_data}, 200)
        except Exception as e:
            return make_response({"error": f"Something went wrong: {e}"}, 400)
