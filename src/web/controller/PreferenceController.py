from flask import (
    request,
    Blueprint)
from flask_cors import cross_origin

from src.model.exception.InvalidInputException import InvalidInputException
from src.repository.dao.PreferenceDao import PreferenceDao
from src.service.PreferenceService import PreferenceService
from src.web.controller.UtilController import UtilController
from src.web.dto.PreferenceDto import PreferenceDto
from src.web.validator.PreferenceValidator import PreferenceValidator

preference_controller = Blueprint('PreferenceController', __name__)

preference_dao: PreferenceDao = PreferenceDao()

service: PreferenceService = PreferenceService(
    preference_dao=preference_dao
)

@cross_origin()
@preference_controller.route('/preference/like', methods=['POST'])
def add_like():
    response: dict
    status_code: int = 200
    try:
        if not PreferenceValidator.validate(request.json):
            raise InvalidInputException("Invalid input.")
        preferenceDto: PreferenceDto = PreferenceValidator.toDto(request.json)

        response = {
            "status": service.add_like(preferenceDto)
        }
    except Exception as exception:
        status_code = 500
        response = UtilController.build_error_payback(exception, status_code)

    return UtilController.build_response(response, status_code)

@cross_origin()
@preference_controller.route('/preference/dislike', methods=['POST'])
def add_dislike():
    response: dict
    status_code: int = 200
    try:
        if not PreferenceValidator.validate(request.json):
            raise InvalidInputException("Invalid input.")
        preferenceDto: PreferenceDto = PreferenceValidator.toDto(request.json)

        response = {
            "status": service.add_dislike(preferenceDto)
        }
    except Exception as exception:
        status_code = 500
        response = UtilController.build_error_payback(exception, status_code)

    return UtilController.build_response(response, status_code)