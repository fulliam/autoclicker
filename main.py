import pyautogui
import time

# Установите количество кликов (например, 500 кликов)
num_clicks = 3700

# Рассчитаем интервал между кликами
interval = 1 / (num_clicks * 40)

# Таймер перед началом работы (например, 5 секунд)
print("Скрипт начнет работать через 5 секунд...")
time.sleep(5)


# Засечение времени старта
start_time = time.time()

# Выполнение кликов
for i in range(num_clicks):
    pyautogui.click()
    time.sleep(int(interval))  # Задержка между кликами

# Подсчет и вывод времени работы скрипта
end_time = time.time()
elapsed_time = end_time - start_time

elapsed_time_int = int(elapsed_time)

clicks_per_second = int(num_clicks / elapsed_time_int)

print(f"Время выполнения: {elapsed_time_int} секунд")
print(f"Приблизительное количество кликов в секунду: {clicks_per_second}")
