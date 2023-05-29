import json

import isodate


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


def parse_duration(duration: str) -> float:
    """Преобразовать строку в формате ISO 8601 в число, представляющее продолжительность в секундах."""
    duration_td = isodate.parse_duration(duration)
    return duration_td.total_seconds()
