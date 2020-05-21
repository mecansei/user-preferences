from flask import (
    Blueprint)

from src.service.AppService import AppService
from src.web.controller.UtilController import UtilController
from flask_swagger_ui import get_swaggerui_blueprint

app_controller = Blueprint('AppController', __name__)
service: AppService = AppService()

swagger_url: str = '/swagger'
swagger_api_definition: str = '/static/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
    swagger_url,
    swagger_api_definition,
    config={
        'app_name': "mecansei/user-preferences"
    }
)


class AppController:
    @staticmethod
    @app_controller.route('/health', methods=['GET'])
    def health():
        is_health, response = service.health_checker()

        return UtilController.build_response(response, 200 if is_health else 503)