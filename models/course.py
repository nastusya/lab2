from models import db


class CourseModel(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(35), nullable=False)
    course_duration = db.Column(db.Date, nullable=False)
    course_language = db.Column(db.String(35), nullable=False)

    course_status_id = db.Column(
        db.Integer,
        db.ForeignKey('course_status.course_status_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )

    course_status = db.relationship('CourseStatusModel', foreign_keys=course_status_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
