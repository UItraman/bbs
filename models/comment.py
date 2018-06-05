from . import ModelMixin
from . import db
from . import timestamp
import time

class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    created_time = db.Column(db.String(), default=0)
    #
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    auth_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        # created_time
        format = '%Y/%m/%d %H:%M:%S'
        v = timestamp() + 3600 * 8
        valuegmt = time.gmtime(v)
        dt = time.strftime(format, valuegmt)
        self.created_time = dt

    def valid(self):
        if len(self.content) > 0:
            return True
        else:
            return False
