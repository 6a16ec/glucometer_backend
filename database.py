import datetime

from peewee import PostgresqlDatabase, PrimaryKeyField, DateTimeField
from peewee import Model, BigIntegerField
from peewee import TextField, DateField, IntegerField
from peewee import ForeignKeyField
import os
from dotenv import load_dotenv

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('POSTGRES_DB'),
    host=os.getenv('POSTGRES_HOST'),
    port=os.getenv('POSTGRES_PORT'),
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    autorollback=True
)

id = BigIntegerField(unique=True)


class Profile(Model):
    id = PrimaryKeyField()
    user_id = TextField()

    class Meta:
        database = db
        db_table = 'profile'


class Measurements(Model):
    id = PrimaryKeyField()
    profile = ForeignKeyField(Profile, backref='user')
    value = IntegerField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        db_table = 'measurements'


if __name__ == '__main__':
    db.connect()
    db.create_tables([Profile, Measurements])
