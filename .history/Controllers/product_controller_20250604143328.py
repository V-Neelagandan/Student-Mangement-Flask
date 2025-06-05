from app import app
from Model.student_model import Student
from flask import render_template, request
from flask import redirect, url_for, flash
import requests

calling_student = Student()

@app.route("/")
def Home():
    response = requests.get("http://127.0.0.1:5000/students")
    student_data = response.json()["Student_data"]
    print(student_data)
    return render_template("index.html", Students=student_data, title="Student Dashboard")

@app.route("/submitform", methods=['GET', 'POST'])
def add_data():
    if request.method == "POST":
        Student_Name = request.form['Student_Name']
        Student_Age = request.form['Student_Age']
        Student_Contact_Email = request.form['Student_Contact_Email']
        Student_Contact_Number = request.form['Student_Contact_Number']

        student_data = {
            "Student": Student_Name,
            "Student_Age": Student_Age,
            "Student_Contact_Email": Student_Contact_Email,
            "Student_Contact_Number": Student_Contact_Number
        }
        response = requests.post(
            "http://127.0.0.1:5000/students", json=student_data)
        if response.status_code == 200:
            return render_template('message.html', title='Data Added Successsfully')
        
        else:
            return render_template('message.html', title='Failed to add student data')
        
    return render_template('form.html', title='Add Details')


@app.route("/students")
def get_student():
    return calling_student.get_student_data()


@app.route('/students', methods=["POST"])
def post_student():
    return calling_student.post_student_data()

@app.route('/students/<id>', methods=["PUT"])
def update_student(id):
    return calling_student.update_student_data(id)


@app.route('/students/<id>', methods=["DELETE"])
def delete_student(id):
    return calling_student.delete_student_data(id)


@app.route('/students/<id>')
def get_student_id(id):
    return calling_student.get_Student_data_By_id(id)

@app.route('/delete/<int:id>', methods=['GET'])
def Delete_student(id):
    response = requests.delete(f'http://127.0.0.1:5000/students/{id}')
    if response.status_code == 200:
       flash('Student deleted successfully', 'success')  # 👈 Flash message
       return redirect('/') # 👈 Redirect to homepage
    else:
        return render_template('message.html', title='Error',message='Failed to delete student')
     
