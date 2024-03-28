from ..models.AdHocEquip import AdHocEquipModel
import requests


def param_config(name, data):
    try:
        adHocEquip_ip = AdHocEquipModel.find_by_name(name).ip
    except:
        return {"message": f"adHocEquip {name} not found."}, 404
    requests.post(f"http://{adHocEquip_ip}/config", json=data)
    return {"message": "config completed."}, 200

    # adHocEquip = AdHocEquipModel.find_by_name(name)
    # if adHocEquip:
    #     ip = adHocEquip.ip
    #     requests.post(f"http://{ip}/config", json=data)
    #     return {"message": "ok"}
