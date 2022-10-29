from operator import itemgetter


class Conductor:

    def __init__(self, id, fio, salary, orchestra_id):
        self.id = id
        self.fio = fio
        self.salary = salary
        self.orchestra_id = orchestra_id


class Orchestra:

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Conductor_Orchestra:
    def __init__(self, orchestra_id, conductor_id):
        self.orchestra_id = orchestra_id
        self.conductor_id = conductor_id


# Отделы
orchestras = [
    Orchestra(1, 'Royal Concertgebouw Orchestra'),
    Orchestra(2, 'Berlin Philharmonic Orchestra'),
    Orchestra(3, 'Vienna Philharmonic Orchestra'),

    Orchestra(11, 'London Symphony Orchestra'),
    Orchestra(22, 'Bavarian Radio Symphony'),
    Orchestra(33, 'Los Angeles Philharmonic'),
]

# Сотрудники
conductors = [
    Conductor(1, 'Артамонов', 25000, 1),
    Conductor(2, 'Петров', 35000, 2),
    Conductor(3, 'Иваненко', 45000, 3),
    Conductor(4, 'Иванов', 35000, 11),
    Conductor(5, 'Иванин', 25000, 22),
    Conductor(6, 'Грозный', 25000, 33),
]

conductors_orchestras = [
    Conductor_Orchestra(1, 1),
    Conductor_Orchestra(2, 2),
    Conductor_Orchestra(3, 3),
    Conductor_Orchestra(3, 4),
    Conductor_Orchestra(3, 5),

    Conductor_Orchestra(11, 1),
    Conductor_Orchestra(22, 2),
    Conductor_Orchestra(33, 3),
    Conductor_Orchestra(33, 4),
    Conductor_Orchestra(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(e.fio, e.salary, d.name)
                   for d in orchestras
                   for e in conductors
                   if e.orchestra_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.orchestra_id, ed.conductor_id)
                         for d in orchestras
                         for ed in conductors_orchestras
                         if d.id == ed.orchestra_id]

    many_to_many = [(e.fio, e.salary, dep_name)
                    for dep_name, dep_id, emp_id in many_to_many_temp
                    for e in conductors if e.id == emp_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in orchestras:
        # Список сотрудников отдела
        d_emps = list(filter(lambda i: i[2] == d.name, one_to_many))
        # Если отдел не пустой
        if len(d_emps) > 0:
            # Зарплаты сотрудников отдела
            d_sals = [sal for _, sal, _ in d_emps]
            # Суммарная зарплата сотрудников отдела
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))

    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for d in orchestras:
        if 'Orchestra' in d.name:
            # Список сотрудников отдела
            d_emps = list(filter(lambda i: i[2] == d.name, many_to_many))
            # Только ФИО сотрудников
            d_emps_names = [x for x, _, _ in d_emps]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.name] = d_emps_names

    print(res_13)


if __name__ == '__main__':
    main()
