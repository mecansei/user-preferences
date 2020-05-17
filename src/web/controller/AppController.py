import json

from flask import (
    Blueprint)

app_controller = Blueprint('AppController', __name__)


class AppController:
    @staticmethod
    @app_controller.route('/health', methods=['GET'])
    def health():
        response = {
            "Application": "Up"
        }
        return json.dumps(response), 200, {'Content-Type': 'application/json'}
