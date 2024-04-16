
class ZDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)


class Session:
    def __init__(self, date, teacher, group, discipline):
        self.date = date
        self.teacher = teacher
        self.group = group
        self.discipline = discipline

    def __str__(self):
        return f"{self.date} у {self.group} будет экзамен по {self.discipline} с {self.teacher}"


# Пример использования классов
sessions = [
    Session(ZDate(13, 4, 2024),
            "Воробьевой Анастасией Александровной", "П1-20", "базам данных"),
    Session(ZDate(17, 4, 2024),
            "Поповым Вячеславом Николаевичем", "П1-20", "технологии разработки ПО"),
    Session(ZDate(12, 4, 2024),
            "Воробьевой Анастасией Александровной", "П1-20", "базам данных")
]

# Вывод графика сдачи экзаменов
print("Расписание экзаменов:")
for session in sorted(sessions, key=lambda x: x.date):
    print(session)
