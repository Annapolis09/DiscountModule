from student_registry_stub import StudentRegistryStub

class DiscountModule:
    STUDENT_DISCOUNT_PERCENT = 15
    CARD_LENGTH = 8

    def __init__(self, registry=None):
        self.registry = registry or StudentRegistryStub()

    def apply_student_discount(self, card_id):
        normalized, error = self._normalize_card_id(card_id)
        if error:
            return self._result(False, 0, error)

        if self.registry.is_expired(normalized):
            return self._result(False, 0, "Срок действия студенческого билета истёк")

        if not self.registry.is_active(normalized):
            return self._result(False, 0, "Студенческий билет не найден в реестре")

        return self._result(
            True,
            self.STUDENT_DISCOUNT_PERCENT,
            f"Билет подтверждён, скидка {self.STUDENT_DISCOUNT_PERCENT}% применена",
        )

    def _normalize_card_id(self, card_id):
        if card_id is None:
            return None, "Номер студенческого билета не указан"
        if isinstance(card_id, bool) or not isinstance(card_id, (str, int)):
            return None, "Неверный тип данных: номер билета должен быть строкой или целым числом"

        if isinstance(card_id, int):
            if card_id < 0:
                return None, "Неверный формат: номер билета не может быть отрицательным"
            card_id = str(card_id).zfill(self.CARD_LENGTH)

        card_id = card_id.strip()

        if card_id == "":
            return None, "Номер студенческого билета не указан"

        if len(card_id) != self.CARD_LENGTH or not card_id.isdigit() or not card_id.isascii():
            return None, f"Неверный формат номера: ожидается {self.CARD_LENGTH} цифр"

        return card_id, None

    @staticmethod
    def _result(success, percent, message):
        return {"success": success, "discount_percent": percent, "message": message}
