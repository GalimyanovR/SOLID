from abc import ABC, abstractmethod

class Pizza:
    def __init__(self):
        self.size: str = ""
        self.dough: str = ""
        self.sauce: str = ""
        self.cheese: str = ""
        self.toppings: list[str] = []

    def __str__(self) -> str:
        toppings = ', '.join(self.toppings) if self.toppings else 'без топпингов'
        return (
            f"Пицца {self.size} на {self.dough} тесте\n"
            f"Соус: {self.sauce}, Сыр: {self.cheese}\n"
            f"Топпинги: {toppings}"
        )

# Интерфейс строителя
class PizzaBuilder(ABC):
    @abstractmethod
    def set_size(self, size: str):
        pass

    @abstractmethod
    def set_dough(self, dough: str):
        pass

    @abstractmethod
    def set_sauce(self, sauce: str):
        pass

    @abstractmethod
    def set_cheese(self, cheese: str):
        pass

    @abstractmethod
    def add_topping(self, topping: str):
        pass

    @abstractmethod
    def build(self) -> Pizza:
        pass

# Конкретный строитель
class ConcretePizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._size = ""
        self._dough = ""
        self._sauce = ""
        self._cheese = ""
        self._toppings = []

    def set_size(self, size: str):
        self._size = size
        return self

    def set_dough(self, dough: str):
        self._dough = dough
        return self

    def set_sauce(self, sauce: str):
        self._sauce = sauce
        return self

    def set_cheese(self, cheese: str):
        self._cheese = cheese
        return self

    def add_topping(self, topping: str):
        self._toppings.append(topping)
        return self

    def build(self) -> Pizza:
        if not self._size:
            raise ValueError("Размер пиццы не указан")
        if not self._dough:
            raise ValueError("Тип теста не указан")

        pizza = Pizza()
        pizza.size = self._size
        pizza.dough = self._dough
        pizza.sauce = self._sauce
        pizza.cheese = self._cheese
        pizza.toppings = self._toppings.copy()

        self.reset()
        return pizza

# Директор с рецептами стандартных пицц
class Director:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def build_margherita(self) -> Pizza:
        return (
            self.builder
            .set_size("L")
            .set_dough("традиционное")
            .set_sauce("томатный")
            .set_cheese("моцарелла")
            .build()
        )

    def build_pepperoni(self) -> Pizza:
        return (
            self.builder
            .set_size("L")
            .set_dough("традиционное")
            .set_sauce("томатный")
            .set_cheese("моцарелла")
            .add_topping("пепперони")
            .build()
        )

    def build_vegetarian(self) -> Pizza:
        return (
            self.builder
            .set_size("M")
            .set_dough("тонкое")
            .set_sauce("песто")
            .set_cheese("пармезан")
            .add_topping("грибы")
            .add_topping("перец")
            .add_topping("оливки")
            .build()
        )

# Клиентский код
director = Director(ConcretePizzaBuilder())
print("Маргарита")
print(director.build_margherita())
print("\nПепперони")
print(director.build_pepperoni())
print("\nВегетарианская")
print(director.build_vegetarian())

print("\nПроизвольная пицца")
pizza = ConcretePizzaBuilder().set_size("XL").set_dough("тонкое").add_topping("грибы").build()
print(pizza)