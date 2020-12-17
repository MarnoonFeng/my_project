import tornado.ioloop  # 核心IO循环模块
import tornado.web  # Web框架模块
import tornado.options  # 解析终端参数模块
from tornado.options import options, define

from handlers.http_handler.sewage_handler import SewageHandler

define(name='port', type=int, default=8080)
urls = [(r'/(\d*)', SewageHandler)]


if __name__ == '__main__':
    # 解析命令行参数
    tornado.options.parse_command_line()
    # 创建应用实例
    app = tornado.web.Application(urls)
    # 监听端口
    app.listen(options.port)
    # 创建IOLoop实例并启动
    print('http服务启动')
    tornado.ioloop.IOLoop.current().start()
