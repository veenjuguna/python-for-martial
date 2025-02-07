import time
import os

class Cat:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def walk(self):
        while True:
            self.position += 1
            self.display()
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        print(" " * self.position + "🐱")

if __name__ == "__main__":
    my_cat = Cat("Whiskers")
    my_cat.walk()
    # sghjkmxcvbnm,.xdbhnm
    # sdfghjkldgfhm,.xcvbnm
    # sfghjk.lkjhsdhjjk
    # sghjkmxcvbnm,.xdbhnm
    # sdfghjkldgfhm,.xcvbnm
    #   edhb sxnkdsxzbjsdbuijk dsuihk sdcvxb msvxcbk sdvcxh
    # fghsdmakzxhjbd asujhbk ndsavjkmdsuixbjh xcz md cx

    # dsaukm dascyhzjn dcduosjkz xhjnsdcbujkn dcdhxc zuijkdn dshxj hfikzxhjnfjzkbdkjacx
   '
#    euadfgickxzkondaucjk sda
# gbasklnzuojadfuhjkm diojbc hebdaoudbdqjas' 