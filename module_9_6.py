def all_variants(text):
    n = len(text)
    for x in range(1, n + 1):
        for j in range(n - x + 1):
            yield text[j:j + x]


a = all_variants("abc")
for i in a:
    print(i)
    