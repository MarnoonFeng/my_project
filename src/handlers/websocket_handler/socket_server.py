import socket
import threading
import time
import logging

from handlers.http_handler.mongo_conn import MongoModel

SOCKET_SETTINGS = {
    'ip': '127.0.0.1',
    'port': 29090,
    'max_size': 128
}


# tcp长连接服务器
class SocketServer(object):

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((SOCKET_SETTINGS.get('ip'), SOCKET_SETTINGS.get('port')))
        self.socket.listen(SOCKET_SETTINGS.get('max_size'))
        self.my_set = MongoModel().get_collection(name='datas')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()

    def run(self):
        while True:
            # 开始接受客户端连接
            conn, addr = self.socket.accept()
            # 开启线程
            logging.info('A Client CONNECTED!')
            t = threading.Thread(target=self.receiv_data, args=(conn, addr))
            t.start()

    def receiv_data(self, conn, addr):
        while True:
            data = conn.recv(1024).decode('utf8')
            # print(data)
            if not data:
                # 空数据
                time.sleep(0.01)
                continue
            else:
                # 数据存入数据库
                try:
                    logging.info('存入数据:>>>>>{}'.format(data))
                    self.my_set.insert_one(eval(data))
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    with SocketServer() as my_server:
        print('长连接服务器启动')
        my_server.run()
