import threading
from time import sleep

# Начальное количество врагов (всем рыцарям)
ENEMIES = 100
lock = threading.Lock()


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        global ENEMIES
        with lock:
            print(f"{self.name}, на нас напали!")

        while ENEMIES > 0:
            sleep(1)
            self.days += 1
            with lock:
                if ENEMIES > 0:
                    ENEMIES -= self.power
                    if ENEMIES > 0:
                        print(f"{self.name}, сражается {self.days} день(дня)..., осталось {max(0, ENEMIES)} воинов.")
                    else:
                        ENEMIES = 0
                        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")
                        break


# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения всех потоков
first_knight.join()
second_knight.join()

print("Все битвы закончились!")