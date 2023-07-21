import logging

# Конфигурация логгера
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Настройка форматирования вывода лога
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# Создание обработчика лога для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
# Добавление обработчика лога к логгеру
logging.getLogger('').addHandler(console_handler)

# Имитация работы программы
for i in range(5):
    try:
        result = 10 / (i - 3)
        logging.info(f"Success: {result}")
    except Exception as e:
        logging.error(f"Exception occurred: {e}", exc_info=True)
