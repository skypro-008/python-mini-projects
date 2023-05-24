from disp_tools import top, frequency

def count_words(filename: str) -> dict:
    """ Подсчитывает количество слов в файле.
        Возвращает словарь, содержащий количество каждого слова в файле.
    """

    word_count = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    return word_count


def main():
    filename = "example.txt"
    word_count = count_words(filename)

    print('Топ 5 слов')
    top(5, word_count)

    print('Слова, встречающиеся не менее 2000 раз')
    frequency(word_count, 2000)



if __name__ == "__main__":
    main()
