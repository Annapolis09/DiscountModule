from student_registry_stub import StudentRegistryStub

class DiscountModule:
    def __init__(self, registry=None):
        self.registry = registry or StudentRegistryStub()

    def apply_student_discount(self, card_id):
        number = int(card_id)

        if self.registry.is_active(str(number)):
            return {"success": True, "discount_percent": 15,
                    "message": "Скидка 15% применена"}

        return {"success": False, "discount_percent": 0,
                "message": "Студенческий билет не найден"}
