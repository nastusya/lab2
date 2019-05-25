from models import db


class CourseStatusModel(db.Model):
    __tablename__ = 'course_status'

    course_status_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    status = db.Column(db.String(35), nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
