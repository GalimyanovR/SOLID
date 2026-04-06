import json
from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class Order:
    id: str
    price: float
    qty: int
    customer_email: str

# Загрузчик
class OrderLoader:
    @staticmethod
    def load_orders_from_json(json_path: str) -> List[Dict[str, Any]]:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)

# Валидация-парсинг
class OrderParser:
    @staticmethod
    def parse_and_validate(raw_data: List[Dict[str, Any]]) -> List[Order]:
        orders = []
        for item in raw_data:
            if "id" not in item or "price" not in item or "qty" not in item or "email" not in item:
                raise ValueError("Invalid order payload")
            if item["qty"] <= 0:
                raise ValueError("qty must be positive")
            orders.append(Order(item["id"], float(item["price"]), int(item["qty"]), item["email"]))
        return orders

# Калькулятор
class OrderCalculator:
    @staticmethod
    def calculate_total(orders: List[Order]) -> float:
        return sum(o.price * o.qty for o in orders)

# Форматтер
class ReportFormatter:
    @staticmethod
    def format_report(orders: List[Order], total: float) -> str:
        return f"Orders count: {len(orders)}\nTotal: {total:.2f}\n"

# Отправка
class EmailSender:
    @staticmethod
    def send_email(to: str, subject: str, body: str) -> None:
        print(f"[EMAIL to={to}] {subject}\n{body}")

class OrderReportService:
    def __init__(self, loader: OrderLoader, parser: OrderParser,
                 calculator: OrderCalculator, formatter: ReportFormatter,
                 sender: EmailSender):
        self.loader = loader
        self.parser = parser
        self.calculator = calculator
        self.formatter = formatter
        self.sender = sender

    def make_and_send_report(self, json_path: str) -> str:
        raw_data = self.loader.load_orders_from_json(json_path)
        orders = self.parser.parse_and_validate(raw_data)
        total = self.calculator.calculate_total(orders)
        report = self.formatter.format_report(orders, total)

        for o in orders:
            self.sender.send_email(o.customer_email, "Your order report", report)

        return report