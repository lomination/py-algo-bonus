# 3.2


def arthur_longest_alpha_substring(s):
    l = len(s)
    r = "", 0
    current = "", 0
    if l > 0:
        current = r = s[0], 1
    for i in range(1, l):
        if s[i - 1] > s[i]:
            current = "", 0
        current = current[0] + s[i], current[1] + 1
        if current[1] > r[1]:
            r = current
    return r


def adam_f_longest_alpha_substring(s: str) -> tuple[str, int]:
    max_len = 0
    max_index = 0
    cur_len = 0
    cur_char = s[0]
    for i in range(len(s)):
        c = ord(s[i])
        if c == current + 1:
            current += 1
        else:
            if current > maximum:
                maximum = current
                index = i - current + 96
            if c == 97:
                current = 97
            else:
                current == 96
    res = ""
    for i in range(96, maximum):
        res += chr(i)
    return (res, index)


test_suite = [
    (("abcdef", 6), ("vdkjhsfjhikdabcdef",)),
]

# TEST = Test()
# TEST.set_func(alpha_substring)
# TEST.unit(("abcdef", 6), ("vdkjhsfjhikdabcdef",))
# TEST.end()
