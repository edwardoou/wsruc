from flask import Blueprint

home = Blueprint('home_blueprint', __name__)

@home.route('/', methods=['GET'])
def get_home():
    return 'API running'
