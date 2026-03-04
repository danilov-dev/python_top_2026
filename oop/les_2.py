class Car:
    def __init__(self, brand: str, model: str, year: int, is_available_sale:bool=True):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_available_sale = is_available_sale
        self.car_type = "passenger car"
        self._is_power = False
        self._is_moove = False

    @property
    def is_power(self):
        return self._is_power

    def get_info(self):
        print(f"Марка: {self.brand} модель: {self.model} год выпуска: {self.year}")

    def power_on(self):
        if self._is_power:
            print("Автомобиль уже заведен")
            return
        print(f"Автомобиль {self.brand} {self.model} заведен")
        self._is_power = True

    def power_off(self):
        if not self._is_power:
            print("Автомобиль уже заглушен")
            return
        print(f"Автомобиль {self.brand} {self.model} заглушен")
        self._is_power = False

    def car_go(self):
        if self._is_moove:
            print("Автомобиль уже в движении")
            return
        print(f"Автомобиль {self.brand} {self.model} поехал")
        self._is_moove = True

    def car_stop(self):
        if not self._is_moove:
            print("Автомобиль уже остановлен")
            return
        print(f"Автомобиль {self.brand} {self.model} остановился")
        self._is_moove = False

    def __repr__(self):
        return f"Car({self.brand}, {self.model}, {self.year}, {self.is_available_sale}, {self.car_type})"



car_1 = Car(brand="Lada", model="Vesta", year=2025)
car_2 = Car("BMW", "M3", 2021, False)

cars = [car_1, car_2]
for car in cars:
    car.power_on()
cars[0].power_off()
cars[1].car_go()
cars[1].car_stop()
