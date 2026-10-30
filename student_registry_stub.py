class StudentRegistryStub:
    ACTIVE_CARDS = {"12345678", "87654321", "20240001", "00123456"}

    EXPIRED_CARDS = {"11111111", "20190042"}

    def is_active(self, card_id: str) -> bool:
        return card_id in self.ACTIVE_CARDS

    def is_expired(self, card_id: str) -> bool:
        return card_id in self.EXPIRED_CARDS