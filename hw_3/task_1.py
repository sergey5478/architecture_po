"""Реализация DIP.
Car принимает engine, как параметр конструктора.
Основной класс не зависит от реализаций,
он зависит от абстракции."""

from abc import ABC, abstractmethod


# Абстрактный класс двигателя
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


# Подклассы бензинового и дизельного двигателей
class GasolineEngine(Engine):
    def start(self):
        print("Запуск бензинового двигателя")


class DieselEngine(Engine):
    def start(self):
        print("Запуск дизельного двигателя")


# Класс машины с инъекцией зависимости двигателя
class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр бензинового двигателя
    gasoline_engine = GasolineEngine()

    # Создаем машину с бензиновым двигателем
    car_with_gasoline_engine = Car(gasoline_engine)
    car_with_gasoline_engine.start_engine()

    # Аналогично для дизельного двигателя
    diesel_engine = DieselEngine()
    car_with_diesel_engine = Car(diesel_engine)
    car_with_diesel_engine.start_engine()
