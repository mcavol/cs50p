from seasons import get_mins
import pytest

def main():
    test_correct()
    test_word()
    test_incorrect()
    test_future()


def test_correct():
    assert get_mins("1994-04-21") == "Fifteen million, seven hundred seventy thousand, eight hundred eighty"

def test_word():
    with pytest.raises(SystemExit) as e:
        get_mins("cat")
    assert str(e.value) == "not valid date"

def test_incorrect():
    with pytest.raises(SystemExit) as e:
        get_mins("2020-02-30")
    assert str(e.value) == "not valid date"

def test_future():
    with pytest.raises(SystemExit) as e:
        get_mins("2024-04-21")
    assert str(e.value) == "date from future"



if __name__ == "__main__":
    main()
