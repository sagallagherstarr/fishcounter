# handlers/user.py

from tornado.log import access_log, app_log, gen_log

from tornado_restful import status
from tornado_restful.exceptions import NotFoundError
from tornado_restful.handlers import APIHandler

from backend.dbconfig import dbManager

from backend.models.sushidatasource import SUSHIDataSource, headerData
from backend.serializers.sushidatasourceserializer import SUSHIDataSourceSerializer

class SUSHIDataSourceHandler(APIHandler):
    async def list(self):
        access_log.debug("SUSHIDataSourceHandler.list")
        # limit, offset = self.paginate()
        async with dbManager.atomic():
            app_log.debug("in atomic context manager")
            sources = await dbManager.execute(SUSHIDataSource.select())

            app_log.debug("sources is %r", sources)
            total = await dbManager.count(SUSHIDataSource.select())
            app_log.debug("count is %r", total)

        app_log.debug("calling serializer")
        serializer = SUSHIDataSourceSerializer(sources, many=True)
        app_log.debug("serializer retutned. Data are %r", serializer.data)
        self.set_status(status.HTTP_200_OK)
        return self.finish({"total": total, "results": serializer.data, "headerData": headerData})

    async def retrieve(self, pk):
        suds = await self.get_object(pk)
        serializer = SUSHIDataSourceSerializer(suds)
        self.set_status(status.HTTP_200_OK)
        return self.finish(serializer.data)

    async def create(self):
        serializer = SUSHIDataSourceSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        await serializer.save()
        self.set_status(status.HTTP_201_CREATED)
        return self.finish(serializer.data)

    async def partial_update(self, pk):
        suds = await self.get_object(pk)
        serializer = SUSHIDataSourceSerializer(suds, self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        await serializer.save()
        self.set_status(status.HTTP_200_OK)
        return self.finish(serializer.data)

    async def destroy(self, pk):
        suds = await self.get_object(pk)
        await self.application.db.delete(suds)
        self.set_status(status.HTTP_204_NO_CONTENT)
        return self.finish()

    async def get_object(self, pk):
        try:
            suds = await dbManager.get(SUSHIDataSource, id=pk)
        except SUSHIDataSource.DoesNotExist:
            raise NotFoundError
        return suds