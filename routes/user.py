from models.user import User
# from models.topic import Topic
from routes import *


main = Blueprint('user', __name__)

Model = User


@main.route('/')
def login_view():
    # ms = Model.query.all()
    return render_template('user_login.html')


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    user = Model.query.filter_by(username=u.username).first()
    if u.valid_login(user):
        session.permanent = True
        session['uid'] = user.id
        return redirect(url_for('index.index'))
    else:
        return redirect(url_for('.login_view'))


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    if u.valid():
        u.save()
        session.permanent = True
        session['uid'] = u.id
        return redirect('/node/')
    else:
        return redirect(url_for('.login_view'))


@main.route('/logout')
def logout():
    p = session.pop('uid')
    print('logout: pop uid', p)
    return redirect(url_for('index.index'))


@main.route('/update_password', methods=['POST'])
def update_password():
    u = current_user()
    password = request.form.get('password', '')
    print('password', password)
    if u.change_password(password):
        print('修改成功')
    else:
        print('用户密码修改失败')
    return redirect('/profile')


@main.route('/update_avatar', methods=['POST'])
@login_required
def update_avatar():
    u = current_user()
    avatar = request.form.get('avatar', '')
    print('password', avatar)
    if u.change_avatar(avatar):
        print('修改成功')
    else:
        print('用户密码修改失败')
    return redirect('/profile')


@main.route('/profile', methods=['GET'])
def profile():
    u = current_user()
    if u is not None:
        print('profile', u.id, u.username, u.password)
        return render_template('user_profile.html', user=u)
    else:
        return redirect(url_for('.login_view'))
