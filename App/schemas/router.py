from ..exts import ma
from ..models.router import RouterModel


class RouterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RouterModel
        load_only = ("id",)


