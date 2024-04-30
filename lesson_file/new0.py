class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f'{self.name} is flying')

    def eat(self):
        print(f'{self.name} is eating')

    def sing(self):
        print(f'{self.name} says {self.voice}')

    def info(self):
        print (f'{self.name} - имя')
        print (f'{self.voice} - голос')
        print (f'{self.color} - цвет')

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food

    def walk(self):
        print(f'{self.name} is walking')

bird_2 = Bird('Кукушка', 'Кря-кря', 'Красный')

bird_1 = Pigeon('Гоша', 'Курлык', 'Серый', 'Хлебные крошки')

bird_1.sing()
bird_1.info()
bird_1.walk()
bird_2.walk()
