import pytest

@pytest.mark.smoke
def test_decor_1():
    assert True

@pytest.mark.regress
def test_decor_2():
    assert True

@pytest.mark.regress
def test_decor_3():
    assert True

@pytest.mark.regress
def test_decor_4():
    assert True

def test_ex():
    a = 1
    assert a in [2, 3, 4]