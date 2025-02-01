class Stone:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def __str__(self):
        return f"Stone(weight={self.weight}, color={self.color})"

# Example usage
stone = Stone(5, "gray")
print(stone)