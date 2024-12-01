

def jerome_longest_palindromic_substring(s):
    length = len(s)
    res = 0
    for i in range(1, length - 1):
        d = 1
        temp = 1
        while i - d > 0 and i + d < length and s[i - d] == s[i + d]:
            temp += 2
            d += 1
        if temp > res:
            res = temp
    return res
