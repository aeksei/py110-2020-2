import random

template = [[192], [168], [10, 20, 30, (100, 200), "150-200"], []]


def gen_ip(template):
    ip_list = []
    for oct_ in template:
        if oct_:
            ip_list.append(oct_)

        else:
            ip_list.append(list(range(256)))

    # ip_list = [[192], [168], [10, 20, 30], list(range(256))]
    return ".".join(map(str, map(random.choice, ip_list)))


for i in range(20):
    print(gen_ip(template))

