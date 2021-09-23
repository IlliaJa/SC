def compress(input: str):
    res = ''
    for char in input:
        if len(res) > 2 and char == res[-2]:
            res = res[:-1] + str(int(res[-1]) + 1)
        else:
            res += f'{char}1'
    if len(res) > len(input):
        res = input
    return res


if __name__ == '__main__':
    for s in ['lol', 'lool', 'looooool']:
        print(compress(s))
