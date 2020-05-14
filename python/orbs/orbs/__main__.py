import sys
from orbs.orbs import ORBSlicer


def main():
    argv = []

    if sys.argv[0] == 'python':
        argv = sys.argv[2:]
    else:
        argv = sys.argv[1:]

    print(argv)
    orbs = ORBSlicer()

    if argv[0][:-4] == 'test':
        orbs.set_pytest

    filepath = argv[0]
    arguments = argv[1:]

    orbs.setup(filepath, arguments)
    orbs.do_slicing()


if __name__ == "__main__":
    main()
