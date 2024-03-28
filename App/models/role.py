from functools import wraps
from ..exts import db, get_jwt_identity
from ..models.user import UserModel


class RoleModel(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    permissions = db.Column(db.Integer, nullable=False)

    users = db.relationship("UserModel", lazy="dynamic")

    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    @classmethod
    def find_by_name(cls, name: str) -> "RoleModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id: int) -> "RoleModel":
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def permission_required(cls, permission):
        def decorator(f):
            @wraps(f)
            def decorated_function(*args, **kwargs):
                user_id = get_jwt_identity()
                user = UserModel.find_by_id(user_id)
                perm = RoleModel.find_by_id(user.role_id).permissions
                if not perm == permission:
                    return {"message": "You don't have the permission."}
                return f(*args, **kwargs)

            return decorated_function

        return decorator

    @classmethod
    def admin_required(cls, f):
        return RoleModel.permission_required(Permission.ADMIN)(f)

    @classmethod
    def manager_required(cls, f):
        return RoleModel.permission_required(Permission.MANAGER)(f)


class Permission:
    VISITOR = 1
    MANAGER = 2
    ADMIN = 4
