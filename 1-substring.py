from testlib import Test


# FUNCTIONS


def substring_ref(s1: str, s2: str) -> int:
    return s1.index(s2) if s2 in s1 else -1


def adam_f_substring(s: str, sub: str) -> int:
    s_len = len(s)
    sub_len = len(sub)
    i = 0
    found = False
    while not found and i <= s_len - sub_len:
        j = 0
        while j < sub_len and s[i + j] == sub[j]:
            j += 1
        if j >= sub_len:
            found = True
        else:
            i += 1
    if found:
        return i
    else:
        return -1


def jerome_substring(s: str, sub: str) -> int:
    i = 0
    result = -1
    length = len(s) - len(sub) + 1
    sub_length = len(sub)
    while result == -1 and i < length:
        j = 0
        while j < sub_length and s[i + j] == sub[j]:
            j += 1
        if j == sub_length:
            result = i
        else:
            i += 1
    return result


def arthur_substring(string, substring):
    result = -1
    main_length = len(string)
    substr_length = len(substring)
    i = 0
    
    while result == -1 and i + substr_length <= main_length:
        delta = -1
        j = 0
        
        while j < substr_length and substring[j] == string[i + j]:
            j += 1
            if j < substr_length and delta == -1 and string[i + j] == substring[j]:
                delta = j
                
        if j == substr_length:
            result = i
        if delta != -1:
            i += delta
        else:
            i += j + 1
            
    return result


def samuel_substring(s, sub):
    r = 0
    len1 = len(s)
    len2 = len(sub)
    if len2 > len1: # error case cuz the substring can't be bigger than it's parent smh
        r = -1 
    else:
        for i in range(len1 - len2 + 1): # taille de la s - taille de la sub...
            isSub = True                           # ..."+ 1" psk on commence à 0 avec "range()"
            j = 0
            while j < len2:
                if s[i+j] != sub[j]:
                    isSub = False
                j += 1
            if isSub == True: # smh we can't use break so I had to use a boolean to get out of the loop
                r = i               
        else:
            r = -1
    return r


def adam_g_substring(s, sub):
    string_len = len(s)
    sub_len = len(sub)
    stop_index = string_len - sub_len
    searching = True
    i = 0
    while i <= stop_index and searching:
        sub_index = 0
        while sub_index < sub_len and s[i + sub_index] == sub[sub_index]:
            sub_index += 1
        searching = sub_index != sub_len
        i += 1
    if searching:
        return -1
    else:
        return i - 1


# TESTS


test_suite = [
    (2, ("hello world", "llo")),
    (-1, ("hello world", "lle")),
    (4, ("hello world", "o world")),
    (0, ("hello world", "hello world")),
    (10, ("hello world", "d")),
    (14, ("cdzFOENKrrxHejVtmPpj", "V")),
    (3 , ("abcabcabcdefdefabcfeddef", "abcabcdef")),
    (16, ("abcabcdfghiabcdeabcdefghiklo", "abcdef")),
    (100000, ("a" * 100000 + "b", "b")),
    (-1, ("a" * 200000, "b")),
    (0, ("longstring" * 50000, "longstring")),
    (250000, ("x" * 250000 + "y" + "z" * 250000, "y")),
    (750000, ("abc" * 250000 + "xyz" + "def" * 250000, "xyz")),
    (300000, ("a" * 300000 + "b" * 300000, "b" * 10)),
    (1000000, ("a" * 1000000 + "end", "end")),
    (499988, ("abcde" * 99999 + "f", "deabcdef")),
    (0, ("1234567890" * 100000, "1234567890")),
    (900000, ("-" * 900000 + "target" + "-" * 100000, "target")),
    (500000, ("x" * 500000 + "match" + "y" * 500000, "match")),
    (-1, ("z" * 1000000, "xy")),
    (0, ("abc" * 333333, "abcabc")),
    (999999, ("123" * 333333 + "456" * 333333, "456")),
    (700000, ("a" * 700000 + "bc" * 100000, "bcbcbc")),
    (0, ("abcd" * 250000 + "xyz", "abcd")),
    (1000000, ("A" * 1000000 + "BBBBB" + "C" * 1000000, "BBBBB")),
    (0, ("pattern" * 250000, "patternpattern")),
    (123456, ("0" * 123456 + "0123456789" * 100000, "0123456789")),
    (999999, ("A" * 999999 + "END", "END")),
    (2000000, ("a" * 2000000 + "b", "b")),
    (-1, ("1" * 5000000, "2")),
    (5000000, ("x" * 5000000 + "yz", "yz")),
    (0, ("huge" * 2500000, "hugehuge")),
    (14999994, ("qwerty" * 2499999 + "asdf" + "uiop" * 2500000, "asdf"))
]


res = Test.speed_test(
    [
        substring_ref,
        adam_f_substring,
        jerome_substring,
        arthur_substring,
        adam_g_substring
        # samuel_substring # has to pass the tests
    ],
    test_suite,
    3
)
