def is_palindrome(input: str):
    return input == input[::-1]

def args_are_similar(str1, str2):
    def get_char_counts(input_str):
        res = {}
        for char in input_str:
            if input_str in res:
                res[char] += 1
            else:
                res[char] = 1
        return res
    return get_char_counts(str1) == get_char_counts(str2)


if __name__ == '__main__':
    for s in ['lol', 'Lool']:
        print(is_palindrome(s))
    for t in [('Illia', 'iallI'), ('illia ', 'Illia ')]:
        print(args_are_similar(*t))
