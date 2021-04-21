# models

# from peewee import BooleanField, DateTimeField

from peewee import Model
from tornado_restful.models.fields import (
    BooleanField,
    DateTimeField,
)

class ModelBase(Model):
    active = BooleanField(default=True)
    inactive_date = DateTimeField(null=True, default=None)

    headerNames = ["Unique ID", "Active", "Inactive date"]