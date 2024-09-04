import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Объект Lock для блокировки потоков
        self.print_lock = threading.Lock()  # Блокировка для синхронизации вывода
        self.deposit_done = threading.Event()  # Флаг для контроля очередности операций

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # Случайная сумма для пополнения
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount  # Увеличиваем баланс
                with self.print_lock:  # Блокируем вывод
                    print(f"Пополнение: {amount}. Баланс: {self.balance}")
            self.deposit_done.set()  # Устанавливаем флаг, что операция пополнения завершена
            time.sleep(0.001)  # Имитация задержки операции
            self.deposit_done.clear()  # Сбрасываем флаг

    def take(self):
        for _ in range(100):
            self.deposit_done.wait()  # Ждем, пока пополнение завершится
            amount = random.randint(50, 500)  # Случайная сумма для снятия
            with self.print_lock:  # Блокируем вывод
                print(f"Запрос на снятие: {amount}")
            with self.lock:  # Блокируем доступ к балансу
                if amount <= self.balance:  # Проверяем достаточно ли средств
                    self.balance -= amount  # Уменьшаем баланс
                    with self.print_lock:  # Блокируем вывод
                        print(f"Снятие: {amount}. Остаток на счете: {self.balance}")
                else:
                    with self.print_lock:  # Блокируем вывод
                        print("Запрос отклонён, недостаточно средств")
            time.sleep(0.001)  # Имитация задержки операции


if __name__ == "__main__":
    bank = Bank()

    # Создаем и запускаем потоки
    deposit_thread = threading.Thread(target=bank.deposit)
    take_thread = threading.Thread(target=bank.take)

    deposit_thread.start()
    take_thread.start()

    # Ожидаем завершения потоков
    deposit_thread.join()
    take_thread.join()

    print(f"Финальный баланс: {bank.balance}")
