def collatz_list(n):
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n
        if n == 1:
            break


if __name__ == '__main__':
    n = 27
    print(list(collatz_list(n)))
