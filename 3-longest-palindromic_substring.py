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

def alex_longest_palindromic_substring(s: str) -> int:
    length = len(s)
    pal_l = length #to save computation, we start by checking the biggest len, and we stop at the first palindrome
    notFound = True
    while notFound and pal_l > 1:
        i = 0 #palindrome position
        while notFound and i < length - (pal_l - 1):
            front_i = i
            back_i = i + (pal_l - 1)
            #checking if this substring is a palindrome:
            while front_i < back_i and s[front_i] == s[back_i]:
                front_i += 1
                back_i -= 1
            notFound = front_i < back_i
            i += 1
        #palindrome length decreases cuz we didn't one yet
        pal_l -= 1
    return pal_l + 1 #because we did -1 during the last iteration. (we could save a tiny grain of computation by putting +1 at the start but at the cost of visibility) 



# TESTS

TEST = Test()
TEST.set_func(longest_palindromic_substring)
TEST.unit(3, ("aabab",))
TEST.unit(5, ("fndskjfkayakdsfjhkf",))
TEST.end()