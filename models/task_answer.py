from models import db


class TaskAnswerModel(db.Model):
    __tablename__ = 'task_answer'

    task_answer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_answer = db.Column(db.String(35), nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.user_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    user = db.relationship('UserModel', foreign_keys=user_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
