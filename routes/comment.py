from models.comment import Comment
from routes import *


main = Blueprint('comment', __name__)

Model = Comment


@main.route('/add', methods=['POST'])
@login_required
def add():
    form = request.form
    u = current_user()
    m = Model(form)
    m.topic_id = int(form.get('topic_id'))
    m.auth_id = u.id
    if m.valid():
        m.save()
    else:
        print('评论不能为空')
    # change topic.comments_num
    m.topic.comments_num += 1
    m.topic.save()
    return redirect(url_for('topic.show', id=m.topic_id))
