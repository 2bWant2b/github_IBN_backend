from ..exts import db


class RouterModel(db.Model):
    __tablename__ = "routers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    ip = db.Column(db.String(30), unique=True, nullable=False)

    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
