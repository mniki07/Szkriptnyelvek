from ekezetekeltv import eltv


def test_eltv():
    assert eltv('át') == 'at'
    assert eltv('átadó') == 'atado'
    assert eltv('kutya') == 'kutya'
    assert eltv('árulás') == 'arulas'
    assert eltv('ŐÚŰ') == 'OUU'
    assert eltv('ioe') == 'ioe'
