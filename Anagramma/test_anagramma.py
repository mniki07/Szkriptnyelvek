from anagramma import anagramma, anagramma1


def test_anagramma():
    assert anagramma("Este", "eset") == True
    assert anagramma("Debit card", "Bad credit") == True
    assert anagramma("Vacation time", "I am not active") == True
    assert anagramma("Astronomers","No more stars") == True


def test_anagramma1():
    assert anagramma1("Este", "eset") == True
    assert anagramma1("Debit card", "Bad credit") == True
    assert anagramma1("Vacation time", "I am not active") == True
    assert anagramma1("Astronomers", "No more stars") == True