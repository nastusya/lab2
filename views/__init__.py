from flask import *
from main import app
from models import *
import csv


@app.before_first_request
def create_tables():
    db.drop_all(app=app)
    db.create_all(app=app)

    fieldnames = ['user_id', 'name', 'average_score', 'email', 'finished_courses', 'courses_in_progress',
                  'price_count']

    dict_reader = csv.DictReader(open('E:/laba2/data.csv', 'r'), fieldnames=fieldnames, delimiter=',', quotechar='"')

    for row in dict_reader:
        user_item = UserModel(
            user_id=int(row['user_id']),
            name=row['name'],
            average_score=int(row['average_score']),
            email=row['email'],
            finished_courses=int(row['finished_courses']),
            courses_in_progress=int(row['courses_in_progress']),
            price_count=int(row['price_count'])
        )

        db.session.add(user_item)

        db.session.commit()


@app.route('/users', methods=['GET'])
def index():
    users_list = UserModel.query.all()

    return render_template("index.html", users_list=users_list)


@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        new_user = UserModel(
            name=request.form['name'],
            email=request.form['email'],
            average_score=request.form['averageScore'],
            courses_in_progress=request.form['progress'],
            finished_courses=request.form['finishedCourses'],
            price_count=request.form['price']
        )
        new_user.save_to_db()

        return redirect('/users')

    return render_template("add-user.html")


@app.route('/remove-user/<int:user_id>', methods=['GET'])
def remove_user(user_id):
    UserModel.query.filter_by(user_id=user_id).delete()
    db.session.commit()

    return redirect('/users')


@app.route('/edit-user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user_item = UserModel.query.filter_by(user_id=user_id).first()

    if request.method == 'POST':
        user_item.name = request.form['name']
        user_item.average_score = request.form['averageScore']
        user_item.email = request.form['email']
        user_item.courses_in_progress = request.form['progress']
        user_item.finished_courses = request.form['finishedCourses']
        user_item.price_count = request.form['price']

        db.session.commit()

        return redirect('/users')

    return render_template("edit-user.html", user_id=user_id, name=user_item.name,
                           average_score=user_item.average_score, email=user_item.email,
                           courses_in_progress=user_item.courses_in_progress,
                           finished_courses=user_item.finished_courses, price_count=user_item.price_count)
