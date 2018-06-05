from models.topic import Topic
from routes import *

from functools import wraps

from routes.user import current_user


main = Blueprint('topic', __name__)

Model = Topic


def login_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        u = current_user()
        if u is None:
            return redirect(url_for('user.login_view'))
        return f(*args, **kwargs)
    return function


@main.route('/')
def index():
    ms = Model.query.all()
    # ms = Model.query.order_by(Model.id.desc()).all()
    return render_template('topic_index.html', topic_list=ms)


@main.route('/new')
@login_required
def new():
    return render_template('topic_new.html')


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    m.read_num += 1
    m.save()
    return render_template('topic.html', topic=m)


@main.route('/edit/<id>')
def edit(id):
    t = Model.query.get(id)
    return render_template('topic_edit.html', todo=t)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    u = current_user()
    m = Model(form)
    m.node_id = int(form.get('node_id'))
    m.auth_id = u.id
    if m.valid():
        m.save()
    else:
        print('主题不能为空')
    return redirect(url_for('node.show', id=m.node_id))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    t = Model.query.get(id)
    t.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
def delete(id):
    t = Model.query.get(id)
    t.delete()
    return redirect(url_for('.index'))
