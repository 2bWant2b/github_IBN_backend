import inspect
from ..exts import db


class AdHocEquipModel(db.Model):
    __tablename__ = "AdHocEquips"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    ip = db.Column(db.String(30), unique=True, nullable=False)
    freqDefault = db.Column(db.Integer, unique=False, nullable=False)
    baudrateRs485 = db.Column(db.Integer, unique=False, nullable=False)
    audioMicGain = db.Column(db.Integer, unique=False, nullable=False)
    pwAtten1 = db.Column(db.Integer, unique=False, nullable=False)
    pwAtten2 = db.Column(db.Integer, unique=False, nullable=False)
    uartBaudrate0 = db.Column(db.Integer, unique=False, nullable=False)
    uartBaudrate1 = db.Column(db.Integer, unique=False, nullable=False)
    uartBaudrate2 = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, name, ip, freqDefault, baudrateRs485, audioMicGain, pwAtten1,
                 pwAtten2, uartBaudrate0, uartBaudrate1, uartBaudrate2):
        self.name = name
        self.ip = ip
        self.freqDefault = freqDefault
        self.baudrateRs485 = baudrateRs485
        self.audioMicGain = audioMicGain
        self.pwAtten1 = pwAtten1
        self.pwAtten2 = pwAtten2
        self.uartBaudrate0 = uartBaudrate0
        self.uartBaudrate1 = uartBaudrate1
        self.uartBaudrate2 = uartBaudrate2

    @classmethod
    def find_by_name(cls, name: str) -> "AdHocEquipModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_init_params(cls):
        init_signature = inspect.signature(cls.__init__)
        return list(init_signature.parameters.keys())[1:]

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
