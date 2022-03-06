from szamjegyek_osszege import ossz

def test_ossz():
    assert ossz(16)==7
    assert ossz(2**15)==26
    assert ossz(2**10)==7
    assert ossz(3**3)==9
    assert ossz(3*9)==9
