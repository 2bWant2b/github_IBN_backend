from ..exts import Resource
from ..schemas.router import RouterSchema
from flask import request
from ..utils.intent_executer import intent_execute

intent_schema = RouterSchema()


class Intent(Resource):
    @classmethod
    def post(cls):
        res = request.get_json()
        user_text = res["text"]
        info = intent_execute(user_text)
        return {"message": [info]}
