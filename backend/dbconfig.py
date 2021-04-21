#
# from contextlib import contextmanager

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

import logging

logging.basicConfig()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.debug("begin db.__init__")

import peewee_async

import config

allModels = set()
log.debug("allModels is %s", allModels)

def setupDatabase(database, host=None, port=None, user=None, password=None):
    database = peewee_async.MySQLDatabase(
        database,
        host=host,
        port=port,
        user=user,
        password=password,
    )

    dbManager = peewee_async.Manager(database) # using the default async event loop. Tornado should also be configured to use this loop.
    dbManager.database.allow_sync = False

    with dbManager.allow_sync():
        database.init(config.databaseName)

    return dbManager

def registerModel(klass):
    log.debug("registerModel: klass is %s", klass)
    allModels.add(klass)

    return klass

def createTables(drop_first=False):
    """Because we delay creating the database until
       after modules are imported, we have to bind
       Model classes to the database at this point.
       Fortunately, we're already set up to do that
       """
    dbManager.database.bind(allModels)

    with dbManager.allow_sync():
        if drop_first:
            dbManager.database.drop_tables(allModels, safe=True)

        dbManager.database.create_tables(allModels)

dbManager = setupDatabase(config.databaseName,
                          config.databaseHost,
                          config.databasePort,
                          config.databaseUser,
                          config.databasePassword)