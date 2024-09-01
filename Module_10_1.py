import threading
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Временные интервалы для выполнения функций
start_time = time()

# Вызов функции write_words с разными аргументами
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time()
print(f"Время выполнения функций: {end_time - start_time} секунд")

# Временные интервалы для выполнения потоков
start_time = time()

# Создание потоков для вызова функции write_words с разными аргументами
threads = [
    threading.Thread(target=write_words, args=(10, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(200, 'example7.txt')),
    threading.Thread(target=write_words, args=(100, 'example8.txt'))
]

# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

end_time = time()
print(f"Время выполнения потоков: {end_time - start_time} секунд")