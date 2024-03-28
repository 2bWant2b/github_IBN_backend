from App import create_app
from App.models.user import BLACKLIST
from App.exts import JWTManager

app = create_app()

jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
    return jwt_payload["jti"] in BLACKLIST


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4999)
