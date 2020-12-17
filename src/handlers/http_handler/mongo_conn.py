import json

from pymongo import MongoClient

MONGO_SETTINGS = {
    'uri': 'mongodb://192.168.225.252:27010,192.168.225.253:27010',
    'db_name': 'nic'
}


# 单例mongo连接封装
class MongoModel(object):

    # 单例模式
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MongoModel, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.client = MongoClient(MONGO_SETTINGS.get('uri'))
        self.db = self.client[MONGO_SETTINGS.get('db_name')]

    # 根据名称获取集合
    def get_collection(self, name):
        return self.db[name]


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        from bson import ObjectId
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
