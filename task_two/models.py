from mongoengine import *

connect(db="webdb",
    host="mongodb+srv://ukrcima:567234@mymongo.bpoqivq.mongodb.net/?retryWrites=true&w=majority&appName=MyMongo",
)


class Task(Document):
    completed = BooleanField(default=False)
    message = StringField(max_length=150)
