from models import db


class UserModel(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    average_score = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    finished_courses = db.Column(db.Integer, nullable=False)
    courses_in_progress = db.Column(db.Integer, nullable=False)
    price_count = db.Column(db.Integer, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
