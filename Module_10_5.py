import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    try:
        with open(name, 'r', encoding='utf-8') as f:
            all_data = f.readlines()  # Считываем все строки сразу
        all_data = [line.strip() for line in all_data]  # Убираем пробелы
    except FileNotFoundError:
        print(f"Файл {name} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла {name}: {e}")
    return all_data

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.monotonic()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.monotonic() - start_time
    print(f'{linear_duration:.4f} секунд (линейный)')

    # Многопроцессный вызов
    start_time = time.monotonic()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_duration = time.monotonic() - start_time
    print(f'{parallel_duration:.4f} секунд (многопроцессный)')