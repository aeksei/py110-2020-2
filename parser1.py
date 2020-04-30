import argparse
import copy


def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("start",
                        type=int,
                        help="Начальное значение арифметической прогрессии")

    parser.add_argument("step",
                        type=int,
                        help="Шаг арифметической прогрессии")

    subparsers = parser.add_subparsers(dest="command")

    subparsers = create_show_subparser(subparsers)
    create_save_subparser(subparsers)

    parser.add_argument('-c',
                        '--count',
                        type=int,
                        default=5,
                        help='Количество элементов арифмитической прогрессии')

    return parser


def create_show_subparser(subparsers):
    subparsers_copy = copy.copy(subparsers)
    subparsers_copy.add_parser('show', help="Режим вывода в консоль")

    return subparsers_copy


def create_save_subparser(subparsers):
    save_subparser = subparsers.add_parser('save', help="Режим вывода в файл")

    save_subparser.add_argument('-i',
                                required=True,
                                type=str,
                                dest='output_file',
                                help="Файл для вывода")
