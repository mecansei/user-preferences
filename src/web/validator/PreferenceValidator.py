from jsonschema import validate as jsonschema_validate

from src.library.logger.Logger import Logger
from src.model.exception.InvalidInputException import InvalidInputException
from src.web.dto.PreferenceDto import PreferenceDto


class PreferenceValidator:
    __json_validator: dict = {
        "type": "object",
        "properties": {
            "user_id": {
                "type": "string"
            },
            "product_id": {
                "type": "string"
            }
        },
        "required": ["user_id", "product_id"]
    }

    @staticmethod
    def toDto(content: dict) -> PreferenceDto:
        try:
            return PreferenceValidator.__build(content)
        except Exception:
            raise InvalidInputException("Invalid input.")

    @staticmethod
    def validate(content: dict) -> bool:
        try:
            jsonschema_validate(
                instance=content,
                schema=PreferenceValidator.__json_validator
            )
            return True
        except Exception as exception:
            Logger.error("PreferenceValidator.validate", str(exception))
            return False

    @staticmethod
    def __build(content: dict) -> PreferenceDto:
        return PreferenceDto(
            user_id=content["user_id"],
            product_id=content["product_id"]
        )
