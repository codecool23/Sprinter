from models import BaseModel
from user_story import *
#base drop/create table file
db.connect()

db.drop_tables([UserStory], safe=True)
db.create_tables([UserStory], safe=True)