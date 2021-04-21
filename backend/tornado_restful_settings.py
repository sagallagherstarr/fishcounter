# settings.py
import os

BASE_DIR = os.path.dirname(__file__)

debug = True
secret_key = "******"

routers_path = os.path.join(BASE_DIR, "routers")
api_prefix = "/api"
trailing_slash = False

mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_username = "root"
mysql_password = "******"
mysql_dbname = ""