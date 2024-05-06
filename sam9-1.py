class Tomato:
    # Словарь стадий созревания помидоров
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        # Каждый помидор имеет уникальный индекс и начальную стадию созревания
        self._index = index
        self._state = 0

    def grow(self):
        # Переводит помидор на следующую стадию созревания, если это возможно
        if self._state < len(self.states) - 1:
            self._state += 1

    def is_ripe(self):
        # Проверяет, достиг ли помидор стадии "красный"
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        # Создает список помидоров на кусте
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        # Заставляет каждый помидор на кусте расти
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        # Проверяет, все ли помидоры на кусте созрели
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        # Очищает список помидоров после сбора урожая
        self.tomatoes = []


class Gardener:
    def __init__(self, name, tomato_bush):
        # Садовник имеет имя и куст, за которым он ухаживает
        self.name = name
        self._plant = tomato_bush

    def work(self):
        # Работа садовника заключается в уходе за кустом
        self._plant.grow_all()

    def harvest(self):
        # Садовник собирает урожай, если все помидоры созрели
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран.")
        else:
            print("Не все помидоры созрели. Нужно еще немного подождать.")

    @staticmethod
    def knowledge_base():
        # Статический метод предоставляет общую информацию о садоводстве
        print("Садоводство — отрасль растениеводства, которая занимается производством продукции"
              " многолетних плодовых и ягодных культур,"
              " а также выращиванием декоративных растений.")


# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов
bush = TomatoBush(2)  # Куст с 2 помидорами
gardener = Gardener("Садовник", bush)  # Садовник, ухаживающий за кустом

# Уход за кустом и первая попытка сбора урожая
gardener.work()
gardener.harvest()

# Продолжение ухода за кустом до созревания всех томатов
while not bush.all_are_ripe():
    gardener.work()

# Финальный сбор урожая
gardener.harvest()
