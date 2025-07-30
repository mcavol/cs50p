from plates import is_valid

def test_letters():
    assert is_valid("a123") == False
    assert is_valid("ps1") == True

def test_chars_number():
    assert is_valid("a") == False
    assert is_valid("1") == False
    assert is_valid("pssdfa") == True

def test_numbers():
    assert is_valid("123") == False
    assert is_valid("as12aq") == False
    assert is_valid("ps021") == False
    assert is_valid("pssd10") == True

def test_punctuation():
    assert is_valid(" ps1 ") == False
    assert is_valid("as,12") == False
    assert is_valid("ps_21") == False

