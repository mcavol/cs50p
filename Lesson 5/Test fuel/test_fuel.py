from fuel import convert, gauge
import pytest

def main():
    test_zero_vivision()
    test_value_error()
    test_correct_convert()
    test_correct_gauge()

def test_zero_vivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_correct_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99

def test_correct_gauge():
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

if __name__ == "__main__":
    main()
