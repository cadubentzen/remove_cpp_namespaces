#!/usr/bin/python3


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for s in sys.argv[1:]:
            print(read_source_file(s))
    else:
        print('usage: %s <filename>' % (sys.argv[0]))
