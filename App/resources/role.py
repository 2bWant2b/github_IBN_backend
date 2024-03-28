from flask_restful import Resource
from ..models.role import RoleModel
from ..schemas.role import RoleSchema
from flask import request

role_schema = RoleSchema()
role_list_schema = RoleSchema(many=True)


class Role(Resource):
    @classmethod
    def get(cls, name):
        role = RoleModel.find_by_name(name)
        if role:
            return role_schema.dump(role), 200
        else:
            return {"message": f"role {name} not found."}, 404

    @classmethod
    def post(cls, name):
        if RoleModel.find_by_name(name):
            return {"message": f"role {name} already exists."}, 400

        role_json = request.get_json()
        role_json["name"] = name
        role_data = role_schema.load(role_json)
        role = RoleModel(**role_data)
        try:
            role.save_to_db()
        except:
            return {"message": f"An error occurred while inserting the role {name}."}, 500

        return role_schema.dump(role), 201

    @classmethod
    def delete(cls, name):
        role = RoleModel.find_by_name(name)
        if role:
            role.delete_from_db()
            return {"message": f"role {name} deleted."}, 200

        return {"message": f"role {name} not found."}, 404


class RoleList(Resource):
    @classmethod
    def get(cls):
        return {"roles": role_list_schema.dump(RoleModel.query.all())}, 200
