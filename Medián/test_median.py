from median import med

def test_med():
    assert med([1,2,3,4,5])==3
    assert med([1,2,4,5])==3
    assert med([1,2,4,5,6,7])==4.5
    assert med([1,50,4,5,6,-500,-20])==4