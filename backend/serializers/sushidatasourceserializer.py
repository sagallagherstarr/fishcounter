# from tornado_restful.models import db
from tornado_restful.serializers import Serializer, fields, validate

from backend.models.sushidatasource import SUSHIDataSource

from backend.dbconfig import dbManager

class ModelBaseSerializer(Serializer):
    id = fields.Int(dump_only=True)
    active = fields.Boolean(required=True)
    inactive_date = fields.DateTime()

class SUSHIDataSourceSerializer(ModelBaseSerializer):
    name = fields.String()
    identifier = fields.String(required=True)
    description = fields.String(required=False, allow_none=True)
    contact = fields.String(required=False, allow_none=True)
    status = fields.String(allow_none=True)
    url_template = fields.String(allow_none=True)
    requester_id = fields.String(allow_none=True)
    customer_id = fields.String(allow_none=True)
    requester_name = fields.String(allow_none=True)
    customer_name = fields.String(allow_none=True)
    user_name = fields.String(allow_none=True)
    password = fields.String(allow_none=True)
    requester_email = fields.Email(allow_none=True)
    api_key = fields.String(allow_none=True)
    platform = fields.String(allow_none=True)

    # headerNames = ["Vendor Name",
    #                "Vendor Identifier",
    #                "Description",
    #                "Contact Info",
    #                "Status",
    #                "URL or URL template",
    #                "Requester ID",
    #                "Customer ID",
    #                "Requester Name",
    #                "Customer Name",
    #                "User Name",
    #                "Password",
    #                "Requester Email",
    #                "API Key",
    #                "PLatform"
    #                ]

    async def create(self, validated_data):
        return await dbManager.create(SUSHIDataSource, **validated_data)

    async def update(self, instance, validated_data):
        for i in validated_data:
            setattr(instance, i, validated_data.get("email", getattr(instance, i)))
        # instance.email = validated_data.get("email", instance.email)
        await dbManager.update(instance)
        return instance