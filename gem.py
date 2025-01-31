class Gem:
    def __init__(self, name, color, value):
        self.name = name
        self.color = color
        self.value = value

    def display_info(self):
        return f"Gem: {self.name}, Color: {self.color}, Value: {self.value}"

# Example usage
if __name__ == "__main__":
    ruby = Gem("Ruby", "Red", 1000)
    print(ruby.display_info())