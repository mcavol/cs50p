from bank import value

def test_hello():
    assert value("hello") == 0
    assert value(" Hello, hi, bonjour  ") == 0

def test_h():
    assert value("hi") == 20
    assert value(" H  ") == 20
    assert value(" halo, my name is  ") == 20
    assert value("hi, hello") == 20

def test_random():
    assert value("bonjour, hello") == 100
    assert value("  ") == 100
    assert value("") == 100
    assert value("ku, hi  ") == 100


