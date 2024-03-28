from ..exts import ma
from ..models.role import RoleModel
from ..models.user import UserModel  # 别删
from ..schemas.user import UserSchema


class RoleSchema(ma.SQLAlchemyAutoSchema):
    users = ma.Nested(UserSchema, many=True)

    class Meta:
        model = RoleModel
        dump_only = ("id",)
        include_fk = True

