from flask import render_template, redirect, url_for
from app import app, db
from app.forms import StudentForm, GradeForm
from app.models import Student, Grade

@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_student.html', form=form)

@app.route('/add_grade/<int:student_id>', methods=['GET', 'POST'])
def add_grade(student_id):
    form = GradeForm()
    student = Student.query.get(student_id)
    if form.validate_on_submit():
        grade = Grade(student_id=student_id, subject=form.subject.data, score=form.score.data)
        db.session.add(grade)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_grade.html', form=form, student=student)

@app.route('/delete_grade/<int:grade_id>', methods=['POST'])
def delete_grade(grade_id):
    grade = Grade.query.get_or_404(grade_id)
    db.session.delete(grade)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_student/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))