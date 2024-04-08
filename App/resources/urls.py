from ..resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from ..resources.role import Role, RoleList
from ..resources.AdHocEquip import AdHocEquip, AdHocEquipList
from ..resources.router import Router
from ..resources.intent import IntentTranslate, IntentExecute
from ..resources.test_topology import TestTopology
from ..resources.tcweb import Tcweb
from ..resources.manual.change_agent_ip import ChangeAgentIP
from ..resources.manual.get_agent_info import GetAgentInfo
from ..resources.manual.adhoc_config import AdhocConfig
from ..exts import api


api.add_resource(UserRegister, "/register")
api.add_resource(User, "/user/<int:user_id>")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLogout, "/logout")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(Role, "/role/<string:name>")
api.add_resource(RoleList, "/roles")
api.add_resource(AdHocEquip, "/adhocequip/<string:name>")
api.add_resource(AdHocEquipList, "/adhocequips")
api.add_resource(Router, '/router/<string:name>')
api.add_resource(IntentTranslate, "/intents/translate")
api.add_resource(IntentExecute, "/intents/execute")
api.add_resource(TestTopology, "/topology")
api.add_resource(Tcweb, "/tcweb")
api.add_resource(ChangeAgentIP, "/manual/changeagentip")
api.add_resource(GetAgentInfo, "/manual/getagentinfo")
api.add_resource(AdhocConfig, "/manual/adhocconfig")
