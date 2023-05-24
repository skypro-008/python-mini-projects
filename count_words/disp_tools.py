def top(n, words):
    s_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    for i in range(n):
        if i>=len(s_words): break
        w, c = s_words[i]
        print(f"{w}: {c}")

def frequency(words, n):
    s_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    for w, c in s_words:
        if c >= n: print(f"{w}: {c}")