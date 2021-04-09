import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

log.debug(__name__)

from pathlib import Path

BASE_DIR = Path(__file__).parents[0]

baseDirStr = str(BASE_DIR)

STATIC_DIR = BASE_DIR / "frontend" / "dist"
staticDirStr = str(STATIC_DIR)
log.debug("staticDirStr is '%s'", staticDirStr)

ENTRY_POINT = "/"
# STATIC_ENTRY = "/static/"

# settings.py
# import os

# BASE_DIR = os.path.dirname(__file__)

debug = True
secret_key = "******"

routers_path = os.path.join(BASE_DIR, "routers")
api_prefix = "/api"
trailing_slash = False

mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_username = "fishcounter"
mysql_password = "temppw1"
mysql_dbname = "fishcounter"