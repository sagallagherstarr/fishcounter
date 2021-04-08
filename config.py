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