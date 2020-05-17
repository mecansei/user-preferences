from src.model.preference.Preference import Preference
from src.repository.dao.PreferenceDao import PreferenceDao
from src.web.dto.PreferenceDto import PreferenceDto


class PreferenceService:
    def __init__(self, preference_dao: PreferenceDao):
        self.__preference_dao = preference_dao

    def add_like(self, preference_dto: PreferenceDto) -> bool:
        self.__preference_dao.add_like(
            self.__toDomain(preference_dto)
        )
        return True

    def add_dislike(self, preference_dto: PreferenceDto) -> bool:
        self.__preference_dao.add_dislike(
            self.__toDomain(preference_dto)
        )
        return True

    def __toDomain(self, preference_dto: PreferenceDto) -> Preference:
        return Preference(
            user_id=preference_dto.user_id,
            product_id=preference_dto.product_id
        )
