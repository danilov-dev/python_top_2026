#Определение класса Animal
class Animal:
    # атрибут класса
    host = "Dmitry"
    counter = 0
    # Конструктор класса (вызывается в момент инициализации экземпляра класса)
    # self - это ссылка на сам объект
    def __init__(self, breed:str, name:str, color:str = 'Grey'):
        # Определение атрибутов экземпляра класса
        self.breed = breed
        self.name = name
        self.color = color
        self.country = "Russia"
        Animal.counter += 1

    # функция, написанная внутри класса = МЕТОД ЭКЗЕМПЛЯРА КЛАССА
    # и вызывается для конкретного класса через точку
    def speak(self):
        print(f"Hi, I'm {self.name}, {self.breed}, my color is {self.color}")

    def bye(self, friend: str):
        print(f"Bye, {friend}! {self.name} go to sleep!")
print(Animal.counter)
dog_chappy = Animal(breed="spaniel", name="Chappy")
print(dog_chappy.counter)
cat_barsik = Animal(breed="Sphinx", name="Barsik", color="Pink")
print(cat_barsik.counter)
