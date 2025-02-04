class Doll:
    def __init__(self, name, material, color):
        self.name = name
        self.material = material
        self.color = color
# hheeeelppppppppppppp
    def display_info(self):
        print(f"Doll Name: {self.name}")
        print(f"Material: {self.material}")
        print(f"Color: {self.color}")

# Example usage
if __name__ == "__main__":
    my_doll = Doll("Barbie", "Plastic", "Pink")
    my_doll.display_info()
    # Doll Name: Barbie
    # Material: Plastic