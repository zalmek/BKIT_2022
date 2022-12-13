def print_result(fun):
    print(fun.__name__)

    def wrapper_print_result(*args, **kwargs):
        result = fun(*args, **kwargs)
        if type(result) == dict:
            for k, v in result.items():
                print("%s=%s" % (k, v))
            return result
        elif type(result) == list:
            for i in result:
                print(i)
            return result
        else:
            print(result)
            return result
    return wrapper_print_result


@print_result
def test_1(integer):
    return integer


@print_result
def test_2(str):
    return str


@print_result
def test_3(dict):
    return dict


@print_result
def test_4(list):
    return list


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1(1)
    test_2("iu5")
    test_3({'a': 1, 'b': 2})
    test_4([1, 2])
