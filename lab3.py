import os
import json
import pickle

FILENAME = 'test.txt'
JSON_FILE = 'tmp.json'


def create_file(filename):
    while True:
        string = input("Введите строку:")
        with open(filename, 'a') as f:
            f.write(string)
            f.write('\n')


def read_binary(filename):
    with open(filename, "rb") as f:
        print(f.read())


def to_json_file(obj, filename, indent=4):
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=indent)


def read_from_json(filename):
    with open(filename, 'r') as f:
        print(json.load(f, parse_int=int))


def to_picle_file(obj, filename):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)


def from_picle_file(filename):
    with open(filename, 'rb') as f:
        print(pickle.load(f))


def main():
    # create_file(FILENAME)
    # read_binary(FILENAME)

    # d = {1: 1,
    #      "2": 5,
    #      (5, 7): "test",
    #      "str": [122, 0x123, 123],
    #      "tuple": (1, 2, 3),
    #      "d": {1: 5},
    #      "func": read_binary
    #      }

    # to_json_file(d, JSON_FILE)
    # read_from_json(JSON_FILE)

    # to_picle_file(d, FILENAME)
    # from_picle_file(FILENAME)

    # access_list = [os.F_OK,
    #                os.R_OK,
    #                os.W_OK,
    #                os.X_OK]
    #
    # for permission in access_list:
    #     print(os.access(FILENAME, permission))
    #
    # for permission in access_list:
    #     print(os.access('lab3.py', permission))


    print(os.environ)
    os.environ['PY_DEBUG'] = "False"

    # password = "123123123"
    password = os.environ['MY_PASSWORD']

    if 'PY_DEBUG' in os.environ:
        if os.environ['PY_DEBUG'] == "True":
            for name, value in os.environ.items():
                print(f"{name}: {value}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
