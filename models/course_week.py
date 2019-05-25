from models import db


class CourseWeekModel(db.Model):
    __tablename__ = 'course_week'

    course_week_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    week_deadline = db.Column(db.Date, nullable=False)
    week_number = db.Column(db.Integer, nullable=False)

    course_id = db.Column(
        db.BigInteger,
        db.ForeignKey('course.course_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    course = db.relationship('CourseModel', foreign_keys=course_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
