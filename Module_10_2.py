import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, turn_interval, initial_enemies, enemies_per_day):
        super().__init__()
        self.name = name
        self.enemies = initial_enemies
        self.turn_interval = turn_interval
        self.enemies_per_day = enemies_per_day
        self.days_fought = 0

    def run(self):
        while self.enemies > 0:
            time.sleep(self.turn_interval)
            if self.enemies > 0:
                to_fight = min(self.enemies, self.enemies_per_day)
                self.enemies -= to_fight
                self.days_fought += 1
                print(f"{self.name} побеждает {to_fight} врагов. Осталось врагов: {self.enemies}")

        print(f"{self.name} одержал победу за {self.days_fought} дней!")

# Начальное количество врагов
initial_enemies = 100

print("На нас напали!")

sir_galahad = Knight("Sir Galahad", 1, initial_enemies, 20)
sir_lancelot = Knight("Sir Lancelot", 2, initial_enemies, 10)

sir_galahad.start()
sir_lancelot.start()

sir_galahad.join()
sir_lancelot.join()

print("Все битвы закончились!")