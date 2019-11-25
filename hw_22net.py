class animal:
    name = "безымянное животное"
    weight = 0
    food = 0
    voice = "неразборчивые звуки"
    milk_maker = "no"
    egg_maker = "no"
    wool_maker = "no"

    def make_voice(self):
        print(self.voice)

    def feed(self):
        print(self.name, ": Спасибо что покормил")
        self.food += 1
        self.weight += 0.5

    def take_egg(self):
        if self.egg_maker == "no":
            print("Это животное не дает яиц")
        else:
            if self.food > 0:
                print("Забрал яиц: ", self.food)
                self.food -= self.food
            else:
                print("Сначала покорми меня")

    def take_milk(self):
        if self.milk_maker == "no":
            print("Это животное не дает молока")
        else:
            if self.food > 0:
                print("Забрал молоко: ", self.food, "л.")
                self.food -= self.food
            else:
                print("Сначала покорми меня")

    def cut_sheep(self):
        if self.wool_maker == "no":
            print("Это животное не дает шерсти")
        else:
            if self.food > 0:
                print("Получил шерсть")
                self.food -= self.food
            else:
                print("Сначала покорми меня")


class milk_makers(animal):
    milk_maker = "yes"
    egg_maker = "no"
    wool_maker = "no"


class egg_makers(animal):
    milk_maker = "no"
    egg_maker = "yes"
    wool_maker = "no"


class wool_makers(animal):
    milk_maker = "no"
    egg_maker = "no"
    wool_maker = "yes"


class sheep(wool_makers):
    type_name = "Овца"
    weight = 50
    voice = "БЕЕЕЕ"


class cow(milk_makers):
    type_name = "Корова"
    weight = 350
    voice = "МУ"


class goat(milk_makers):
    type_name = "Коза"
    weight = 50
    voice = "МЕ"


class duck(egg_makers):
    type_name = "Утка"
    weight = 1
    voice = "КРЯ"


class goose(egg_makers):
    type_name = "Гусь"
    weight = 3
    voice = "ГА ГА"


class chicken(egg_makers):
    type_name = "Курица"
    weight = 1
    voice = "Ко-Ко"


def help_command():
    print(
        "Что вы хотите сделать?\n1 - покормить\n2 - взять молока\n3 - собрать яйца\n4 - собрать шерсть\n5 узнать вес\n6 - услышать голос\n7 - выбрать другое животное\n0 - вывести подсказку\n")


goose1 = goose()
goose1.name = "Серый"
goose2 = goose()
goose2.name = "Белый"
cow1 = cow()
cow1.name = "Манька"
sheep1 = sheep()
sheep1.name = "Барашек"
sheep2 = sheep()
sheep2.name = "Кудрявый"
chicken1 = chicken()
chicken1.name = "Ко-ко"
chicken2 = chicken()
chicken2.name = "Кукареку"
goat1 = goat()
goat1.name = "Рога"
goat2 = goat()
goat2.name = "Копыта"
duck1 = duck()
duck1.name = "Кряква"

animal = [goose1, goose2, cow1, sheep1, sheep2, chicken1, chicken2, goat1, goat2, duck1]

name_list = []
for pet in animal:
    name_list.append(pet.name)


def find_out_weight():
    animal_weight = 0
    for pet in animal:
        animal_weight += pet.weight
    print("Вес всех животных на ферме: ", animal_weight)


def find_out_fat():
    fat_animal_weight = 0
    fat_animal = ""
    for pet in animal:
        if pet.weight > fat_animal_weight:
            fat_animal_weight = pet.weight
            fat_animal = pet.name
            fat_type = pet.type_name
        elif pet.weight == fat_animal_weight:
            fat_animal = (fat_animal, pet.name)
    print("Самое толстое животное:")
    print(fat_type, "по имени", fat_animal)


def make_some():
    while True:
        print("Список животных:")
        for pet in animal:
            print(pet.name)
        name = input("Введите имя животного к которому вы хотите подойти(если хотите выйте наберите exit): ")
        if name == "exit":
            break
        elif name not in name_list:
            print("Животного с таким именем нет, попробуйте еще раз")
        else:
            for pet in animal:
                if name == pet.name:
                    help_command()
                    while True:
                        command = input("Что хотите сделать?")
                        if command == "1":
                            pet.feed()
                        elif command == "2":
                            pet.take_milk()
                        elif command == "3":
                            pet.take_egg()
                        elif command == "4":
                            pet.cut_sheep()
                        elif command == "5":
                            print("Вес", pet.name, pet.weight, "кг")
                        elif command == "6":
                            print(pet.name, "говорит: ", pet.voice)
                        elif command == "7":
                            break
                        elif command == "0":
                            help_command()


def menu():
    while True:
        main_menu_command = input(
            "Что вы хотите? \n1 - узнать общий вес животных\n2 - узнать самое толстое животное,\n3 - подойти к животному\n4 - уехать с фермы\n")
        if main_menu_command == "1":
            find_out_weight()
        elif main_menu_command == "2":
            find_out_fat()
        elif main_menu_command == "3":
            make_some()
        elif main_menu_command == "4":
            break


print(
    'Вы приехали на ферму Дядюшки Джо и видите вокруг себя множество разных животных: \nгусей "Серый" и "Белый" \nкорову "Маньку" \nовец "Барашек" и "Кудрявый" \nкур "Ко-Ко" и "Кукареку" \nкоз "Рога" и "Копыта" \nи утку "Кряква')
menu()


