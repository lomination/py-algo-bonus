from testlib import Test


# FUNCTIONS


def longest_palindromic_substring(s: str) -> int:
    res = 0
    length = len(s)
    for i in range(1, length - 1):
        delta = 1
        while i - delta > 0 and i + delta < length and s[i - delta] == s[i + delta]:
            delta += 1
        palin_len = 2 * delta - 1
        if palin_len > res:
            res = palin_len
    return res


# TESTS

TEST = Test()
TEST.set_func(longest_palindromic_substring)
TEST.unit(3, ("aabab",))
TEST.unit(5, ("fndskjfkayakdsfjhkf",))
TEST.end()