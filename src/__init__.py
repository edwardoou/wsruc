from flask import Flask

# Routes
from routes.RucRoutes import ruc
from routes.HomeRoutes import home

app = Flask(__name__)

def init_app():
    # Blueprints
    app.register_blueprint(home, url_prefix='/')
    app.register_blueprint(ruc, url_prefix='/sunat')

    return app