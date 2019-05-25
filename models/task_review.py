from models import db


class TaskReviewModel(db.Model):
    __tablename__ = 'task_review'

    task_review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lector_review = db.Column(db.String(35), nullable=False)

    task_answer_id = db.Column(
        db.Integer,
        db.ForeignKey('task_answer.task_answer_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    task_answer = db.relationship('TaskAnswerModel', foreign_keys=task_answer_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
