#
# main.py
# the main file of the backend / server side of the project

import logging
logging.basicConfig()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

log.debug(__name__)

import asyncio
from tornado.platform.asyncio import AsyncIOMainLoop
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

import config
from tornado_restful.conf import settings as tornado_restful_settings
tornado_restful_settings.routers_path = config.routers_path

from tornado_restful.handlers import NotFoundHandler
# from tornado_restful.models import db
from tornado_restful.shortcuts import get_routes

from tornado.log import access_log, app_log, gen_log


import backend.models.sushidatasource

# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")

def make_app():
    routes = get_routes(config.routers_path, config.api_prefix)

    app = tornado.web.Application(
        routes +
        [(r"/(.*)", tornado.web.StaticFileHandler, {"path": config.staticDirStr, "default_filename": "index.html"})],
        **config.tornadoSettings, default_handler_class=NotFoundHandler)

    return app

def testModelDone():
    log.debug("testModelDone.")

if __name__ == "__main__":
    # AsyncIOMainLoop().install()

    tornado.log.enable_pretty_logging()

    for i in ["access", "application", "general"]:
        l = logging.getLogger("tornado." + i)
        l.setLevel(logging.DEBUG)

    try:
        app = make_app()
        app.listen(8888)
    except OSError:
        pass

    io_loop = tornado.ioloop.IOLoop.current()
    loop = asyncio.get_event_loop()

    loop.create_task(backend.models.sushidatasource.testModel())
    io_loop.start()