from abc import ABC, abstractmethod

# Абстрактный класс Animal
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass

# Класс Lion, наследующий Animal
class Lion(Animal):
    def make_sound(self) -> str:
        return "Рычание!"

# Класс Monkey, наследующий Animal
class Monkey(Animal):
    def make_sound(self) -> str:
        return "Визг!"

# Класс Elephant, наследующий Animal
class Elephant(Animal):
    def make_sound(self) -> str:
        return "Трубление!"

# Абстрактная фабрика AnimalFactory
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

# Фабрика LionFactory
class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()

# Фабрика MonkeyFactory
class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()

# Фабрика ElephantFactory
class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()

# Функция взаимодействия с животным через фабрику
def interact_with_animal(factory: AnimalFactory) -> None:
    animal = factory.create_animal()
    print(f"Звук: {animal.make_sound()}")