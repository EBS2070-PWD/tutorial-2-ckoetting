def count_matching_strings(strings):
    return sum(1 for s in strings if len(s) >= 2 and s[0] == s[-1])
