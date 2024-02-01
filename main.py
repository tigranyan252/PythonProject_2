class Triangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_info(self):
        return f"Поле 1: {self.side1}, Поле 2: {self.side2}"

    def calculate_hypotenuse(self):
        hypotenuse = (self.side1 ** 2 + self.side2 ** 2) ** 0.5
        return hypotenuse


# Пример использования класса в основной программе
side1 = float(input("Введите значение первого катета: "))
side2 = float(input("Введите значение второго катета: "))

triangle = Triangle(side1, side2)

info = triangle.get_info()
hypotenuse = triangle.calculate_hypotenuse()

print("Информация о треугольнике:")
print(info)
print("Длина гипотенузы: ", hypotenuse)

