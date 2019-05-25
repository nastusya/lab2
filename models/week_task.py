from models import db


class WeekTaskModel(db.Model):
    __tablename__ = 'week_task'

    week_task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(35), nullable=False)

    course_week_id = db.Column(
        db.Integer,
        db.ForeignKey('course_week.course_week_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    course_week = db.relationship('CourseWeekModel', foreign_keys=course_week_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
