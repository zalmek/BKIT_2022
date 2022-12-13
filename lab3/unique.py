# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.counter = -1
        if kwargs.get('ignore_case'):
            self.unique = list()
            for i in range(len(items)):
                items[i].lower()
                if items[i] not in self.unique:
                    self.unique.append(items[i])
        else:
            self.unique = list()
            for i in range(len(items)):
                if items[i] not in self.unique:
                    self.unique.append(items[i])

    def __next__(self):
        if self.counter < len(self.unique)-1 and self.unique[self.counter] is not None:
            self.counter += 1
            return self.unique[self.counter]
        else:
            raise StopIteration

    def __iter__(self):
        return self


def main():
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    un = Unique(data)
    un = sorted(un)
    for i in un:
        print(i)
main()