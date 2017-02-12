from peewee import *

#create database
db = PostgresqlDatabase("zahoranszky", user="zahoranszky")


class BaseModel(Model):
    """A base Postgresql database"""
    class Meta:
        database = db