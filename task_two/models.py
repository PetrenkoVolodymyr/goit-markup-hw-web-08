from mongoengine import *

connect(db="webdb",
    host="mongodb+srv://ukrcima:567234@mymongo.bpoqivq.mongodb.net/?retryWrites=true&w=majority&appName=MyMongo",
)


class Task(Document):
    completed = BooleanField(default=False)
    name = StringField(max_length=150)
    email = StringField(max_length=150)
    phone = StringField(max_length=200)
    comm_chan = StringField(max_length=5)
    message = StringField(max_length=150)
