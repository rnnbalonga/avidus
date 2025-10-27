from collections.abc import Iterable

data_list = [1, [2, 3, [4, 5]], (6, 7, [8, [9]]), {10, 11, 12}]

weird_list = [{"name": "Roki", "looks": "cutie"}, 2, 3, [4, 5, [6, (7, 8)]]]

def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x 

def main():
    result_data_list = list(flatten(data_list))
    print(result_data_list)
    
    result_weird_list = list(flatten(weird_list))
    print(result_weird_list)

if __name__ == "__main__":
    main()