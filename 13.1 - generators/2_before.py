def collatz_list(n):
    result = []
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            result.append(n)
        if n == 1:
            break

    return result


if __name__ == '__main__':
    n = 27
    print(len(collatz_list(n)))
