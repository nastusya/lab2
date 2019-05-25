from models import db


class LectorRiviewModel(db.Model):
    __tablename__ = 'lector_review'

    lector_review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lector_review = db.Column(db.String(100), nullable=False)

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey('user.user_id', onupdate='cascade', ondelete='restrict'),
        nullable=False
    )
    user = db.relationship('UserModel', foreign_keys=user_id)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
