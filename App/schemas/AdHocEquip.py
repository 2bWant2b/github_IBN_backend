from ..exts import ma
from ..models.AdHocEquip import AdHocEquipModel


class AdHocEquipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdHocEquipModel
        load_only = ("id",)
