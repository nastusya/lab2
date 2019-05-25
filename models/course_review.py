from models import db


class CourseReviewModel(db.Model):
    __tablename__ = 'course_review'

    course_review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    review = db.Column(db.String(35), nullable=False)

    course_id = db.Column(
        db.Integer,
        db.ForeignKey('course.course_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    course = db.relationship('CourseModel', foreign_keys=course_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
