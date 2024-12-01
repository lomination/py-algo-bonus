from testlib import Test


# FUNCTIONS


def longest_alpha_substring(s: str) -> tuple[str, int]:
    length = len(s)
    res = ("", 0)
    if length > 0:
        current = res = (s[0], 1)
    for i in range(1, length):
        if s[i - 1] > s[i]:
            current = ("", 0)
        current = (current[0] + s[i], current[1] + 1)
        if current[1] > res[1]:
            res = current
    return res


# TEST


TEST = Test()
TEST.set_func(longest_alpha_substring)
TEST.unit(("abcdef", 6), ("vdkjhsfjhikdabcdef",))
TEST.unit(("aaaf", 4), ("aaafeeee",))
TEST.unit(("eeeee", 5), ("aaafeeeee",))
TEST.end()
