from ..exts import Resource
from ..schemas.router import RouterSchema
from flask import request
from ..utils.intent_manager import intent_execute, intent_translate

intent_schema = RouterSchema()


class IntentTranslate(Resource):
    @classmethod
    def post(cls):
        res = request.get_json()
        user_text = res["text"]
        info = intent_translate(user_text)
        return {"message": [info]}


class IntentExecute(Resource):
    @classmethod
    def post(cls):
        res = request.get_json()
        user_text = res["text"]
        info = intent_execute(user_text)
        return {"message": [info]}

