import collections

def removeDuplicateLetters(s):
    if not s: return ""
    counts = collections.Counter(list(s))

    print(s)
    print(counts)

    pos = 0
    for i, x in enumerate(s):
        if x < s[pos]:
            # print(i, x, s[pos])
            pos = i

        counts[x] -= 1
        if counts[x] == 0: break

    print(counts)
    print(pos)



    return s[pos] + removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))


# res = removeDuplicateLetters("cbacdcbca")
res = removeDuplicateLetters("abceabce")
print(res)
