import random


def gen_random(num_count, begin, end):
    list=[]
    for i in range(num_count):
        list.append(random.randint(begin,end))
    return list
def main():
    list = gen_random(10,130,200)
    for i in list:
        print(i)
main()