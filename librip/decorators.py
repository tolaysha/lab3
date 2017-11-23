def print_result(decor):
    def decorated_func(*args):
        result = decor(*args)
        print(decor.__name__)
        if type(result) is str or type(result) is int:
            print(result)
        if type(result) is list:
            list(map(lambda x: print(x), result))
        if type(result) is dict:
            for y, z in result.items():
                print('{} = {}'.format(y, z))
        return result

    return decorated_func
