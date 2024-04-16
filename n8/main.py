class Polynom:
    def __init__(self, coefficients):
        # Конструктор класса, принимает список коэффициентов многочлена
        self.coefficients = coefficients

    def __add__(self, other):
        # Перегрузка оператора сложения для многочленов
        result_coeffs = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        # Проходим по коэффициентам с максимальной длиной
        for i in range(max_len):
            # Если индекс меньше длины текущего многочлена, берем коэффициент,
            # иначе считаем его равным 0
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            # Складываем коэффициенты и добавляем результат в новый список
            result_coeffs.append(coeff1 + coeff2)
        return Polynom(result_coeffs)

    def derivative(self):
        # Метод для нахождения производной многочлена
        result_coeffs = [i * self.coefficients[i] for i in range(1, len(self.coefficients))]
        return Polynom(result_coeffs)

    def __str__(self):
        # Перегрузка метода преобразования объекта в строку
        result = ""
        for i in range(len(self.coefficients) - 1, -1, -1):
            coeff = self.coefficients[i]
            # Пропускаем нулевые коэффициенты
            if coeff != 0:
                # Добавляем знак "+" для положительных коэффициентов,
                # кроме первого члена
                if coeff > 0 and i != len(self.coefficients) - 1:
                    result += "+"
                # Добавляем коэффициент, если он не равен 1 или это свободный член
                if i == 0 or coeff != 1:
                    result += str(coeff)
                # Добавляем "x" для всех членов, кроме свободного
                if i > 0:
                    result += "x"
                # Добавляем степень, если она больше 1
                if i > 1:
                    result += "^" + str(i)
        return result


if __name__ == "__main__":
    p1 = Polynom([1, 2, 3])  # Создаем первый многочлен: 3x^2 + 2x + 1
    p2 = Polynom([4, 5, 6])  # Создаем второй многочлен: 6x^2 + 5x + 4

    print("Первый многочлен:", p1)
    print("Второй многочлен:", p2)

    sum_polynom = p1 + p2  # Складываем два многочлена
    print("Сумма двух многочленов:", sum_polynom)

    derivative_p1 = p1.derivative()  # Находим производную от первого многочлена
    print("Производная от первого многочлена:", derivative_p1)
