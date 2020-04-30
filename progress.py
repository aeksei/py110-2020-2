from parser1 import create_parser


def ar(start=1, step=1):
    n = start
    while True:
        yield n
        n += step


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    print(namespace)

    COUNT = namespace.count

    if namespace.command == 'show':
        gen = ar(namespace.start, namespace.step)
        for _ in range(COUNT):
            print(next(gen))
    elif namespace.command == 'save':
        with open(namespace.output_file, 'w') as f:
            gen = ar(namespace.start, namespace.step)
            for _ in range(COUNT):
                f.write(str(next(gen)))
                f.write('\n')


if __name__ == "__main__":
    main()
