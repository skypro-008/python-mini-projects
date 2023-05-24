import random
import string


def stretch(text: str, max_len: int) -> str:
    """
    Растягивает заданный текст до указанной максимальной длины, добавляя случайные
    символы в конец.

    Args:
        text: Текст для растяжения
        max_len: Максимальная длина возвращаемой строки

    Returns:
        Растянутый текст
    """
    if len(text) < max_len:
        random_char = get_random_char()
        return stretch(text + random_char, max_len)
    else:
        return text


def get_random_char() -> str:
    """
    Возвращает случайно выбранный символ из печатаемых ASCII-символов.
    """
    chars = string.printable
    random_char = chars[random.randint(0, len(chars) - 1)]
    return random_char


def main() -> None:
    """
    Запрашивает у пользователя максимальную длину и повторяет растяжение пустой строки
    до тех пор, пока она не достигнет этой длины. Печатает полученную строку.
    """
    while 1:
        max_len = input(' [?] Enter a length for your password (e for exit): ')
        try:
            maxlength = int(max_len)
            print("'", stretch('', maxlength), "'\n")
        except ValueError:
            if max_len == 'e':
                break
            print('Please Enter an integer')


if __name__ == '__main__':
    main()
