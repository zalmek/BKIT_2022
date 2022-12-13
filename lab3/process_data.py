import json
import gen_random
from lab3 import cm_timer, unique
from lab3.field import field
from lab3.print_result import print_result

path = r"C:\Users\Zalmek\PycharmProjects\pythonProject\lab3\my.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, "r", encoding="UTF-8") as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    from lab3 import unique
    return list(sorted(unique.Unique(field(arg, "job-name"))))


@print_result
def f2(arg):
    return list(filter(lambda x: x[0:11] == "программист", arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return list(zip(arg,gen_random.gen_random(len(arg), 100000, 200000)))
    #return list(map(lambda x: x + ", Зарплата " + str(gen_random.gen_random(1, 100000, 200000)) + " руб.", arg))


if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1(data))))
