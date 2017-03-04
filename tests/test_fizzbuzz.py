from fizzbuzz import fizzbuzz

def test_fizz():
    assert fizzbuzz(3) == 'fizz'

def test_buzz():
    assert fizzbuzz(5) == 'buzz'

def test_fizzbuzz():
    assert fizzbuzz(15) == 'fizzbuzz'

def test_normal():
    assert fizzbuzz(1) == '1'
