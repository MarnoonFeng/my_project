from tornado.web import RequestHandler

from handlers.http_handler.mongo_conn import MongoModel, JSONEncoder


class SewageHandler(RequestHandler):

    def get(self, *args, **kwargs):
        point_id = self.get_argument('PointID')
        count = self.get_argument('count')
        my_set = MongoModel().get_collection(name='datas')
        mn = point_id + '~32_2011'
        result_json = JSONEncoder().encode(my_set.find_one({'code': mn}))

        self.write('查到数据:{}'.format(result_json))
