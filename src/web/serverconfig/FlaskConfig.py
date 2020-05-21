import os

from flask import Flask
from flask_cors import CORS
from flask_selfdoc import Autodoc

from src.web.controller.AppController import app_controller
from src.web.controller.PreferenceController import preference_controller
from src.web.controller.AppController import swagger_blueprint


class FlaskConfig:
    app = Flask(__name__)
    cors = CORS(app)
    auto = Autodoc(app)

    def __call__(self):
        self.register_blue_prints()
        self.run_app()

    def register_blue_prints(self):
        self.app.register_blueprint(app_controller)
        self.app.register_blueprint(preference_controller)
        self.app.register_blueprint(swagger_blueprint, url_prefix="/swagger")

    def run_app(self):
        self.app.run(
            debug=True,
            use_reloader=False,
            host=os.getenv("FLASK_HOST"),
            port=os.getenv("FLASK_PORT")
        )
