def field(dict_arr, *args):
    if len(args) == 1:
        list = []
        for i in range(len(dict_arr)):
            if dict_arr[i].get(args[0]) is not None:
                list.append(dict_arr[i].get(args[0]))
        return list
    else:
        for i in range(len(dict_arr)):
            dict = {}
            for j in range (len(args)):
                if dict_arr[i].get(args[j]) is not None:
                    dict[args[j]]=(dict_arr[i].get(args[j]))
            return dict
def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
    ]
    print(field(goods,'title'))
main()