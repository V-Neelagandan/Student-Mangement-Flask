import sqlite3
from flask import request, make_response


connection_string = sqlite3.connect('College.db', check_same_thread=False)
connection_string.row_factory = sqlite3.Row  # when ur code  response like dict
quary = connection_string.cursor()

# quary.execute("""Create table student(
#     Id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Student_Name VARCHAR(50),
#     Student_Age INTEGER(50),
#     Student_Contact_Number VARCHAR(50),
#     Student_Contact_Email VARCHAR(50)
# )""")
# print('Table Created Successfully!')


class Student:

    def get_student_data(self):
        try:

            quary.execute("SELECT * FROM student")
            Student_data = [dict(data)for data in quary.fetchall()]
            return make_response({"succes": "data retrived sucessfully", "Student_data": Student_data}, 200)

        except Exception as e:
            return make_response({"error": f"something error occured as {e}"}, 400)

    def post_student_data(self):
        data = request.json
        try:
            quary.execute(
                'insert into student(Student_Name,Student_Age,Student_Contact_Number,Student_Contact_email) values(?,?,?,?)', tuple(data.values()))
            connection_string.commit()
            return make_response({"success": "Student Data added succeesssfully!!!"}, 200)
        except Exception as e:
            return make_response({"error": f"something error occured as {e}"}, 400)

    def delete_student_data(self, id):
        id = int(id)
        if id == 0 or id < 0:
            return make_response({'sucess': 'please provide valid id'}, 400)
        try:
            quary.execute(f"delete from student where id={id}")
            connection_string.commit()
            return make_response({"sucess": "student data deleted sucessfully"})
        except Exception as e:
            return make_response({"error": f"something error occured as {e}"}, 400)

    def update_student_data(self, id):
        id = int(id)
        if id == 0 or id < 0:
            return make_response({"success": "please provide valid Id"}, 400)
        data = request.json
        data = list(data.values())
        data.append(id)
        print(data)
        try:
            quary.execute(
                "Update Student Set Student_Name=? ,Student_Age =?,Student_Contact_Number =?,Student_Contact_Email=? where Id=?", tuple(data))
            return make_response({"success": " Data updated succeesssfully!!!"})
        except Exception as e:
            return make_response({"error": f"Somrthing error occured as {e}"}, 400)

    def get_Student_data_By_id(self, id):
        id = int(id)
        try:
            quary.execute(f"Select * from Student Where ID = {id}")
            student_data = [dict(records) for records in quary.fetchall()]
            if student_data == []:
                return make_response({"success": f"Student rocord with ID {id} does't exist"}, 404)
            return make_response({"success": "data retrived successfully!!!","Student_Data": student_data})
        except Exception as e:
            return make_response({"error": f"Something error occured as {e}"}, 400)

# def get_Student_data_By_id(self, id):
    # id = int(id)
    # try:
    #     quary.execute(f"SELECT * FROM Student WHERE ID = {id}")
    #     student_data = [dict(records) for records in quary.fetchall()]
    #     if not student_data:
    #         return make_response({"success": f"Student record with ID {id} doesn't exist"}, 404)
        
    #     return make_response({
    #         "success": "data retrieved successfully!!!",
    #         "Student_data": student_data[0]  # ✅ Return a single student dict
    #     }, 200)
    # except Exception as e:
    #     return make_response({"error": f"Something error occurred as {e}"}, 400)

