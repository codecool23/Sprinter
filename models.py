from peewee import *

#create database for this app
db = PostgresqlDatabase("zahoranszky", user="zahoranszky")


class BaseModel(Model):
    """A base Postgresql database"""
    class Meta:
        database = db