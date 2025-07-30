from twttr import shorten

def test_a():
    assert shorten("ata") == "t"
    assert shorten("AkA") == "k"

def test_e():
    assert shorten("qew") == "qw"
    assert shorten("EfE") == "f"

def test_i():
    assert shorten("pipi") == "pp"
    assert shorten("sIs") == "ss"

def test_o():
    assert shorten("cococ") == "ccc"
    assert shorten("lOl") == "ll"

def test_u():
    assert shorten("uwu") == "w"
    assert shorten("JUL") == "JL"

def test_numbers():
    assert shorten("0987") == "0987"

def test_signs():
    assert shorten("as, qq") == "s, qq"

