from routes import *

main = Blueprint('index', __name__)


@main.route('/')
def index():
    return redirect(url_for('node.index'))
