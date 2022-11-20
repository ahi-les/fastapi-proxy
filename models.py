from peewee import *
import typing
import random
from pydantic import BaseModel
from pydantic import Field

db = SqliteDatabase('database.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = "id"


class Proxy(BaseModel):
    ip = CharField()
    port = IntegerField()
    login = CharField()
    pass_ = CharField()
    active = CharField()
    port_http = IntegerField()
    label = CharField(null=True)


    class Meta:
        db_table = 'proxies'

    def __init__(self):
        self._items: typing.Dict[int, Proxy] = {}  # id: model

    def get_random(self) -> int:
        # Получение случайной фразы
        return random.choice(self._items.keys())

    def get(self, id: int) -> typing.Optional[Proxy]:
        # Получение фразы по ID
        return self._items.get(id)