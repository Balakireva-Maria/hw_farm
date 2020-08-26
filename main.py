class Animals:
    fullness = 'hungry'
    location = 'at home'
    cleanliness = 'dirty'
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

        def feed(self):
            self.fullness = 'full'
            return print('onomnomnom')

        def walking(self):
            self.location = 'outside'

        def wash(self):
            self.cleanliness = 'clean'

        def speak(self):
            return print(self.voice)


class Birds(Animals):
    egg_basket = 'full'

    def get_egg(self):
        self.egg_basket = 'empty'
        return print('you got eggs')


class Chiken(Birds):
    animal_type = 'Курица'
    voice = 'ko-ko-ko'


class Duck(Birds):
    animal_type = 'Утка'
    voice = 'krya-krya-krya'


class Goose(Birds):
    animal_type = 'Гусь'
    voice = 'ga-ga-ga'


class Hornet_cattle(Animals):
    milk = 'full of milk'

    def get_milk(self):
        self.milk = 'you got milk'
        return print('milk is collected')


class Cow(Hornet_cattle):
    animal_type = 'Корова'
    voice = 'moo-moo'


class Goat(Hornet_cattle):
    animal_type = 'Коза'
    voice = 'be-be-be'


class Ship(Animals):
    animal_type = 'Барашек'
    wool = 'a lot'
    voice = 'meeeeeh'

    def cut(self):
        self.wool = 'you got a wool'
        return print('wool is collected')


goose_0 = Goose('Серый', 4)
goose_1 = Goose('Белый', 3.5)

cow = Cow('Манька', 450)

ship_0 = Ship('Барашек', 70)
ship_1 = Ship('Кудрявый', 90)

chiken_0 = Chiken('Ко-Ко', 0.8)
chiken_1 = Chiken('Кукареку', 1)

goat_0 = Goat('Рога', 50)
goat_1 = Goat('Копыта', 45)

duck = Duck('Кряква', 1)

animal_list = [goose_0, goose_1, ship_0, ship_1, cow, chiken_0, chiken_1, goat_0, goat_1, duck]

list_for_weight = []
list_for_name = []

total_weight = 0
for animal in animal_list:
    total_weight = total_weight + animal.weight
    list_for_name.append(animal.animal_type)
    list_for_weight.append(animal.weight)

list1 = list(zip(list_for_weight, list_for_name))

a = (max(list1))
print(f' Самое тяжелое животное на ферме - {a[1]} ')

print(f' Общий вес всех животных на ферме составляет {total_weight} кг')






