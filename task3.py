import random
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception('Need 1 parameter')
    if len(sys.argv) == 2 and not sys.argv[1].isdigit():
        raise Exception('Value of parameter must be an integer')
    num_lines = int(sys.argv[1])
    with open('random_file.txt', 'r') as f:
        all_lines = f.readlines()
        print(all_lines[-num_lines:])
