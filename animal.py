class Zebra:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Neigh"

    def __str__(self):
        return f"Zebra(name={self.name}, age={self.age})"

# Example usage
zebra = Zebra("Marty", 5)
print(zebra)
print(zebra.make_sound())
# ghjasdghjjjjzxcv 