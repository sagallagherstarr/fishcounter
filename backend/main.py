#
# main.py
# the main file of the backend / server side of the project

import logging
logging.basicConfig()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

log.debug(__name__)

from tornado.log import access_log, app_log, gen_log


from typing import (
    Dict,
    Any,
    Union,
    Optional,
    Awaitable,
    Tuple,
    List,
    Callable,
    Iterable,
    Generator,
    Type,
    cast,
    overload,
)

import tornado.ioloop
import tornado.web

from tornado.log import access_log, app_log, gen_log

import config

settings = {
    "debug" : True,
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__", # TODO
    "login_url": "/login",
    "xsrf_cookies": True,
}

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")

def make_app():
    app = tornado.web.Application([
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": config.staticDirStr, "default_filename": "index.html"}),
    ], settings)

    return app

if __name__ == "__main__":
    # tornado.log.setLevel(logging.DEBUG)
    tornado.log.enable_pretty_logging()

    for i in ["access", "application", "general"]:
        l = logging.getLogger("tornado." + i)
        l.setLevel(logging.DEBUG)

    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()