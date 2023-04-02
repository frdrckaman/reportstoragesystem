from os import walk


def file_name(path):
    filenames = next(walk(path), (None, None, []))[2]
    print(filenames)
    with open('fins.txt', 'w') as f:
        for filename in filenames:
            f.write(filename)
            f.write('\n')


def main():
    file_name('/var/log/')


if __name__ == '__main__':
    main()
