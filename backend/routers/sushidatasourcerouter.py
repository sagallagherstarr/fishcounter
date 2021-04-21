# routers/user.py
from tornado_restful.routers import NestedRouter

from backend.handlers.sushidatasourcehandler import SUSHIDataSourceHandler

router = NestedRouter()
router.register(r"sushidatasource", SUSHIDataSourceHandler)