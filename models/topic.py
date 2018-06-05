from . import ModelMixin
from . import db
from . import timestamp
import time


class Topic(db.Model, ModelMixin):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    created_time = db.Column(db.String(), default=0)
    comments_num = db.Column(db.Integer)
    read_num = db.Column(db.Integer)
    # has relationship with comments
    comments = db.relationship('Comment', backref="topic")
    #
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
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
        self.comments_num = 0
        self.read_num = 0

    def valid(self):
        if len(self.title) > 0:
            return True
        else:
            return False
