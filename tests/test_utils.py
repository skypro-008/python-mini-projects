from src.utils import parse_duration


def test_parse_duration():
    assert parse_duration("PT1H") == 3600.0
    assert parse_duration("PT1M") == 60.0
    assert parse_duration("PT1S") == 1.0
    assert parse_duration("PT10.5S") == 10.5
