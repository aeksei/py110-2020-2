import re
import random


def parse_template(raw_template, unique=True):
    # проверка корректности входных данных
    if not isinstance(raw_template, list):
        raise TypeError(f"Шаблон должен быть списком, не {type(raw_template)}")

    if not all(isinstance(oct_, list) for oct_ in raw_template):
        raise TypeError("Шаблон должен включать в себя только списки")

    if len(raw_template) != 4:
        raise ValueError("Шаблон должен быть длины 4!")

    template = []
    for oct_ in raw_template:
        octet_list = []
        if not oct_:
            octet_list.extend(range(256))
        else:
            for item in oct_:
                if isinstance(item, int):
                    octet_list.append(item)
                elif isinstance(item, tuple):
                    octet_list.extend(range(*item))
                    # octet_list.extend(range(item[0], item[1))
                # далее через elif можно продолжать обрабатывать различные типы

        template.append(octet_list)

    if unique:
        unique_template = map(set, template)
        return list(map(list, unique_template))
    else:
        return template


# def filter_ip(fn):
#     def wrapper(*args, **kwargs):
#         # действия до вызова функции
#         result = fn(*args, **kwargs)
#         # действия после вызова функции
#         return result
#     return wrapper

def filter_ip(pattern):
    def decorator_filter_ip(fn):
        ip_pattern = re.compile(pattern)

        def wrapper(*args, **kwargs):
            local_gen = fn(*args, **kwargs)
            for result in local_gen:
                # действия до вызова генератора
                if ip_pattern.fullmatch(result):
                    yield result
                # действия после вызова генератора
        return wrapper
    return decorator_filter_ip


# @filter_ip("192\.168(?:.\d{1,3}){2}")
@filter_ip("10(?:.\d{1,3}){3}")
def gen_ip(raw_template):
    template = parse_template(raw_template)
    while True:
        # TODO сделать корутину
        yield ".".join(map(str, map(random.choice, template)))


def main():
    user_template = [[],
                     [],
                     [],
                     []]
    gen = gen_ip(user_template)

    for i in range(20):
        print(next(gen))


if __name__ == "__main__":
    main()
