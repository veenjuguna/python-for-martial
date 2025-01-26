import time
import os

class Dog:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def run(self):
        while self.position < 50:
            self.position += 1
            self.display_position()
            time.sleep(0.1)

    def display_position(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{self.name} is running: " + " " * self.position + "🐕")

if __name__ == "__main__":
    dog = Dog("Buddy")
    dog.run()