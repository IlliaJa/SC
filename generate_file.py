import random
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Need 1 parameter')
    if len(sys.argv) == 2 and not sys.argv[1].isdigit():
        raise Exception('Value of parameter must be an integer')
    num_lines = int(sys.argv[1])
    with open('random_file.txt', 'w') as f:
        for i in range(num_lines):
            number = random.randint(1, 1_000_000_000)
            f.write(f'{number}\n')
