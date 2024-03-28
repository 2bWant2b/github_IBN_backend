# 定时获取设备信息

from ..exts import scheduler
from ..models.AdHocEquip import AdHocEquipModel
import requests


class DataFetcher:
    def __init__(self, model, name):
        item = AdHocEquipModel.find_by_name(name)
        self.model = model
        self.url = f"http://{item.ip}/config"
        self.key_set = model.get_init_params()

    def fetch_data(self):
        response = requests.get(self.url)
        data = response.json()
        data_fetch = {k: data[k] for k in self.key_set if k in data}
        data_fetch["freqDefault"] = data["freqList"][data["freqDefault"]]

        item = self.model.find_by_name(data_fetch["name"])
        if item:
            item.update(**data_fetch)
            # print("Updated data successfully.")
            return
        item = self.model(**data_fetch)
        item.save_to_db()
        print("Fetched and stored data successfully.")


@scheduler.task('interval', id='job1', seconds=5)
def fetch_adhoc_data():
    with scheduler.app.app_context():
        DataFetcher(model=AdHocEquipModel, name="node40").fetch_data()
