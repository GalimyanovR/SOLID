from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Order:
    total: float

# Асбрактный класс для скидок
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, order: Order) -> float:
        pass

# Скидка 0%
class RegularDiscount(DiscountStrategy):
    def apply(self, order: Order) -> float:
        return order.total

# Скидка 10%
class VipDiscount(DiscountStrategy):
    def apply(self, order: Order) -> float:
        return order.total * 0.9

# Скидка 20%
class EmployeeDiscount(DiscountStrategy):
    def apply(self, order: Order) -> float:
        return order.total * 0.8

# Скидка 50%
class BlackFridayDiscount(DiscountStrategy):
    def apply(self, order: Order) -> float:
        return order.total * 0.5


def apply_discount(order: Order, discount_strategy: DiscountStrategy) -> float:
    return discount_strategy.apply(order)