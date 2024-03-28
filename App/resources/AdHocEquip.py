from flask import request
from ..exts import jwt_required, Resource
from ..utils.param_config import param_config
from ..models.AdHocEquip import AdHocEquipModel
from ..schemas.AdHocEquip import AdHocEquipSchema
from ..models.role import RoleModel
import requests

ADHOCEQUIP_NOT_FOUND = "AdHocEquip {} not found."
NAME_ALREADY_EXISTS = "the AdHocEquip {} already exists."
ERROR_INSERTING = "An error occurred while inserting the AdHocEquip {}."
ADHOCEQUIP_DELETED = "AdHocEquip {} deleted."

adHocEquip_schema = AdHocEquipSchema()
adHocEquip_list_schema = AdHocEquipSchema(many=True)


class AdHocEquip(Resource):
    # @jwt_required()
    # @RoleModel.admin_required
    def get(self, name):
        item = AdHocEquipModel.find_by_name(name)
        if item:
            response = requests.get(f"http://{item.ip}/config")
            data = response.json()
            return data

        return {"message": ADHOCEQUIP_NOT_FOUND.format(name)}, 404

    # @classmethod
    # def post(cls, name):
    #     if AdHocEquipModel.find_by_name(name):
    #         return {"message": NAME_ALREADY_EXISTS.format(name)}, 400
    #
    #     adHocEquip_json = request.get_json()
    #     adHocEquip_json["name"] = name
    #     adHocEquip_data = adHocEquip_schema.load(adHocEquip_json)
    #     adHocEquip = AdHocEquipModel(**adHocEquip_data)
    #
    #     try:
    #         adHocEquip.save_to_db()
    #     except:
    #         return {"message": ERROR_INSERTING.format(name)}, 500  # internal server error
    #
    #     return adHocEquip_schema.dump(adHocEquip), 201  # CREATED
    #
    # @classmethod
    # def delete(cls, name):
    #     adHocEquip = AdHocEquipModel.find_by_name(name)
    #     if adHocEquip:
    #         adHocEquip.delete_from_db()
    #         return {"message": ADHOCEQUIP_DELETED.format(name)}
    #
    #     return {"message": ADHOCEQUIP_NOT_FOUND.format(name)}
    #
    @classmethod
    def post(cls, name):
        adHocEquip_json = request.get_json()
        param_config(name, adHocEquip_json)
        return {"message": "ok"}


class AdHocEquipList(Resource):
    #@jwt_required()
    #@RoleModel.admin_required
    def get(self):
        adHocEquips = adHocEquip_list_schema.dump(AdHocEquipModel.query.all())

        return adHocEquips
