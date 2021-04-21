# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:37:12 2021

@author: scott
"""

"""Model for a vendor, which contains all the information necessary to
make the SUSHI connection.  Supported reports/COUNTER versions is in a
separate table.

Fields:
    -- vendor name
    -- vendor identifier (this helps to separate multiple accounts
                          per vendor)
    -- vendor description
    -- contact information
    -- status [ active/inactive ]
    -- SUSHI request URL template
    -- SUSHI fields:
        -- Requester ID
        -- Customer ID
        -- Requester Name
        -- Customer Name
        -- User Name
        -- Password
        -- Requester Email
        -- API Key
        -- Platform
"""

""" local data, do not distribute!
vendor name = "Annual Reviews"
vendor identifier = "AnnualReviews"
vendor description = "Multiple annual review titles"
contact information = "iops@annualreviews.org"
status = active
SUSHI request URL template = "https://www.annualreviews.org/reports/<COUNTER5 report id>?requestor_id=sgallagherstarr&customer_id=224197&<other parameters>"
Requester ID = "sgallagherstarr"
Customer ID = "224197"
"""
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.debug("begin sushidatasource.py")

import json

from tornado.log import access_log, app_log, gen_log

from tornado_restful.models.fields import (
    CharField,
    TextField,
)
from backend.models import ModelBase

from backend.dbconfig import registerModel, dbManager, createTables

class SUSHIDataSource(ModelBase):
    name = CharField()
    identifier = CharField(unique=True)
    description = TextField(null=True)
    contact = CharField(null=True)
    status = CharField()
    url_template = TextField(null=False)
    requester_id = CharField()
    customer_id = CharField()
    requester_name = CharField()
    customer_name = CharField()
    user_name = CharField()
    password = CharField()
    requester_email = CharField()
    api_key = CharField()
    platform = CharField()

    headerNames = ModelBase.headerNames + [ "Vendor Name",
                    "Vendor Identifier",
                    "Description",
                    "Contact Info",
                    "Status",
                    "URL or URL template",
                    "Requester ID",
                    "Customer ID",
                    "Requester Name",
                    "Customer Name",
                    "User Name",
                    "Password",
                    "Requester Email",
                    "API Key",
                    "Platform"
                  ]

headerData = [
    { "text": i[0], "value": i[1] }
    for i in zip(SUSHIDataSource.headerNames, SUSHIDataSource._meta.sorted_field_names)
]

headerData[0]["align"] = "start"
headerData[0]["sortable"] = True

registerModel(SUSHIDataSource)

async def testModel():
    app_log.debug("testModel")
    createTables(drop_first=True)

    bob = SUSHIDataSource(name="Friendly",
                          identifier="FRIENDLY",
                          description="Rama Llama Ding Dong",
                          contact="888-999-1010",
                          status="For real",
                          url_template="http://www.example.com/SUSHI/?requester_id={requester_id}",
                          requester_id="surelynot",
                          customer_id="example.com",
                          requester_name="James McJames",
                          customer_name="HRH Frances",
                          user_name="George",
                          password="kr**79",
                          requester_email="george@example.com",
                          api_key="77665544332211",
                          platform="R5")

    log.debug("bob is %s\n%r", bob, bob)

    result = await dbManager.create_or_get(SUSHIDataSource, **bob.__data__)

    log.debug("save result is %r", result)

    fred = await dbManager.execute(SUSHIDataSource.select())
    total = await dbManager.count(SUSHIDataSource.select())

    app_log.debug("fred is %r", fred)
    app_log.debug("total is %r", total)