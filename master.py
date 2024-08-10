import pyautogui
import time
import threading
from pynput import keyboard

# Начальные параметры
current_level = 3
current_coins = 77000
coins_per_click = 3  # 3 монеты за клик на 3 уровне
next_level_coins = 250000  # Количество монет для перехода на 4 уровень
final_target = 10000000  # Цель: 10 000 000 монет
num_clicks = 5000  # Максимальное количество кликов за раз
interval_between_clicks = 1 / 8  # Интервал между кликами для 8 кликов в секунду

# Флаг для остановки скрипта
stop_script = False

def stop_clicking():
    global stop_script
    stop_script = True

def on_press(key):
    print(key)
    if key == keyboard.Key.space:
        stop_clicking()
        return False

def calculate_time_to_next_level():
    global current_coins, coins_per_click, next_level_coins

    clicks_needed = (next_level_coins - current_coins) // coins_per_click
    time_needed = clicks_needed / 8  # время в секундах при 8 кликах в секунду
    return time_needed

def calculate_time_to_final_target():
    global current_coins, coins_per_click, final_target

    clicks_needed = (final_target - current_coins) // coins_per_click
    time_needed = clicks_needed / 8  # время в секундах при 8 кликах в секунду
    return time_needed

def start_clicker():  
    global stop_script, current_coins

    # Запуск слушателя для остановки скрипта по нажатию пробела
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Отложенный запуск скрипта через 2 минуты
    time.sleep(10)

    # Засечение времени старта
    start_time = time.time()

    for i in range(num_clicks):
        if stop_script:
            print("Скрипт остановлен пользователем.")
            break
        pyautogui.click()
        current_coins += coins_per_click
        time.sleep(interval_between_clicks)

    # Подсчет и вывод времени работы скрипта
    end_time = time.time()
    elapsed_time = end_time - start_time

    elapsed_time_int = int(elapsed_time)
    clicks_per_second = int(num_clicks / elapsed_time_int)

    print(f"Время выполнения: {elapsed_time_int} секунд")
    print(f"Приблизительное количество кликов в секунду: {clicks_per_second}")
    print(f"Текущие монеты: {current_coins}")

    listener.stop()

# Вычисление времени до следующего уровня и до 10 000 000 монет
time_to_next_level = calculate_time_to_next_level()
time_to_final_target = calculate_time_to_final_target()

print(f"Время до следующего уровня: {time_to_next_level / 3600:.2f} часов")
print(f"Время до 10 000 000 монет: {time_to_final_target / 3600:.2f} часов")

# Запуск кликерного скрипта в отдельном потоке
clicker_thread = threading.Thread(target=start_clicker)
clicker_thread.start()
