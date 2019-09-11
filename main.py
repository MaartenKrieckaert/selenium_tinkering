from datetime import timedelta
from time import time

SCRIPT_START = time()


def main() -> None:
    print('It works!')


if __name__ == '__main__':
    main()
    runtime = time() - SCRIPT_START
    print('Script finished in', timedelta(seconds=runtime))
