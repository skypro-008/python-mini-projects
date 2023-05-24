def print_top_n_words(word_count: dict, n: int) -> None:
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i in range(n):
        if i >= len(sorted_word_count):
            break
        word, count = sorted_word_count[i]
        print(f"{word}: {count}")


def print_words_with_frequency(word_count: dict, min_freq: int) -> None:
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        if count >= min_freq:
            print(f"{word}: {count}")
