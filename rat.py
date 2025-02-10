class Rat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def squeak(self):
        return f"{self.name} says: Squeak!"

    def __str__(self):
        return f"Rat(name={self.name}, age={self.age})"

# Example usage
if __name__ == "__main__":
    rat = Rat("Remy", 2)
    print(rat)
    print(rat.squeak())