import pyautogui
import time
import json
import threading
from pynput import keyboard

class Clicker:
    def __init__(self, config_path="config.json"):
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
        
        self.current_level = config["current_level"]
        self.current_coins = config["current_coins"]
        self.coins_per_click = config["coins_per_click"]
        self.next_level_coins = config["next_level_coins"]
        self.final_target = config["final_target"]
        self.num_clicks = config["num_clicks"]
        self.interval_between_clicks = 1 / config["clicks_per_second"]
        self.stop_script = False


    def stop_clicking(self):
        self.stop_script = True

    def on_press(self, key):
        print(key)
        if key == keyboard.Key.space:
            self.stop_clicking()
            return False

    def calculate_time_to_next_level(self):
        clicks_needed = (self.next_level_coins - self.current_coins) // self.coins_per_click
        time_needed = clicks_needed / 8
        return time_needed

    def calculate_time_to_final_target(self):
        clicks_needed = (self.final_target - self.current_coins) // self.coins_per_click
        time_needed = clicks_needed / 8
        return time_needed

    def start_clicker(self):  
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        print("Waiting 10 seconds before starting...")
        time.sleep(10)

        while not self.stop_script:
            start_time = time.time()

            for i in range(self.num_clicks):
                if self.stop_script:
                    print("Script stopped by the user.")
                    break
                pyautogui.click()
                self.current_coins += self.coins_per_click
                time.sleep(self.interval_between_clicks)

            end_time = time.time()
            elapsed_time = end_time - start_time

            elapsed_time_int = int(elapsed_time)
            clicks_per_second = int(self.num_clicks / elapsed_time_int)

            print(f"Execution time: {elapsed_time_int} seconds")
            print(f"Approximate clicks per second: {clicks_per_second}")
            print(f"Current coins: {self.current_coins}")

            if not self.stop_script:
                print("Waiting 1.5 hours before the next cycle.")
                time.sleep(5400)

        listener.stop()

clicker = Clicker()

clicker_thread = threading.Thread(target=clicker.start_clicker)
clicker_thread.start()
