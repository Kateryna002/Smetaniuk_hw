class Rhombus:
    def __init__(self, сторона_а, кут_а):
        self.сторона_а = сторона_а
        self.кут_а = кут_а   # кут_б встановиться автоматично у __setattr__

    def __setattr__(self, name, value):
        if name == "сторона_а":
            if value <= 0:
                raise ValueError("Сторона 'сторона_а' повинна бути більше 0")
            object.__setattr__(self, name, value)

        elif name == "кут_а":
            if not (0 < value < 180):
                raise ValueError("Кут 'кут_а' повинен бути між 0 і 180")
            object.__setattr__(self, "кут_а", value)
            object.__setattr__(self, "кут_б", 180 - value)

        else:
            object.__setattr__(self, name, value)

    def __str__(self):
        return f"Ромб: сторона = {self.сторона_а}, кут_а = {self.кут_а}, кут_б = {self.кут_б}"
