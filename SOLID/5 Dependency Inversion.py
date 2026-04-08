from abc import ABC, abstractmethod
from typing import List

# Абстракция отправителя уведомлений
class Notifier(ABC):
    @abstractmethod
    def send(self, to: str, text: str) -> None:
        pass

# Реализация email
class EmailNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[EMAIL to={to}] {text}")

# Реализация sms
class SmsNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[SMS to={to}] {text}")

# Пеализация для уведомлений
class PushNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        print(f"[PUSH to={to}] {text}")

# Фейковый отправитель для тестов
class FakeNotifier(Notifier):
    def send(self, to: str, text: str) -> None:
        pass

# Сервис уведомлений зависит от абстракции
class NotificationService:
    def __init__(self, notifiers: List[Notifier]):
        self.notifiers = notifiers

    def notify(self, recipients: List[str], text: str) -> None:
        for notifier in self.notifiers:
            for recipient in recipients:
                notifier.send(recipient, text)