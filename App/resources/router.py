from flask import request
from ..exts import Resource
from ..models.router import RouterModel
from ..schemas.router import RouterSchema

router_schema = RouterSchema()


class Router(Resource):
    @classmethod
    def post(cls, name):
        if RouterModel.find_by_name(name):
            return {"message": f"router {name} already exists."}

        json = request.get_json()
        json["name"] = name
        data = router_schema.load(json)
        router = RouterModel(**data)
        try:
            router.save_to_db()
        except:
            return {"message": f"An error occurred while inserting the role {name}."}, 500

        return router_schema.dump(router), 201
