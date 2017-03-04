import pytest

from fizzbuzz import fizzbuzz

@pytest.fixture(params=(5, 25, 50, 70),
                scope='module')
def numbuzz(request):
    print('Creating fixture num={}'.format(request.param))
    yield request.param
    print('Cleaning fixture num={}'.format(request.param))

#@pytest.fixture(params=('sqlite', 'postgres')
#def db(request):
#    if request.param == 'sqlite':


def test_fizz():
    assert fizzbuzz(3) == 'fizz'

def test_buzz(numbuzz):
    assert fizzbuzz(numbuzz) == 'buzz'

def test_str_buzz(numbuzz):
    assert str(fizzbuzz(numbuzz)) == 'buzz'

def test_fizzbuzz():
    assert fizzbuzz(15) == 'fizzbuzz'

def test_normal():
    assert fizzbuzz(1) == '1'
