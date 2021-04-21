import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

log.debug(__name__)

from pathlib import Path

BASE_DIR = Path(__file__).parents[0]

baseDirStr = str(BASE_DIR)

CONFIG_FILE = str(BASE_DIR / "config.py")

STATIC_DIR = BASE_DIR / "frontend" / "dist"
staticDirStr = str(STATIC_DIR)
log.debug("staticDirStr is '%s'", staticDirStr)

ENTRY_POINT = "/"
# STATIC_ENTRY = "/static/"

# settings.py
# import os

# BASE_DIR = os.path.dirname(__file__)

debug = True
secret_key = "*fink^^beam98%"

# routers_path = os.path.join(BASE_DIR, "routers")
api_prefix = "/api"
routers_path = BASE_DIR / "backend" / "routers"
trailing_slash = False

databaseHost = "127.0.0.1"
databasePort = 3306
databaseUser = "fishcounter"
databasePassword = "temppw1"
databaseName = "fishcounter"
databaseTestName = "fishcounter_test"

tornadoSettings = {
    "debug" : True,
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__", # TODO
    "login_url": "/login",
    "xsrf_cookies": True,
}
