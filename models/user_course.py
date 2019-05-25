from models import db


class UserCourseModel(db.Model):
    __tablename__ = 'user_course'

    user_course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.course_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.user_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )

    course = db.relationship('CourseModel', foreign_keys=course_id)
    user = db.relationship('UserModel', foreign_keys=user_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
