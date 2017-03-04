import pytest

from twitterwall import *


@pytest.fixture(scope='module', params=('foo', 'bar'))
def status(request):
    return {
        'user': {'screen_name': 'username'},
        'text': request.param,
        'entities': {
            'hashtags': [],
            'symbols': [],
            'urls': [],
            'user_mentions': [],
        }
    }


def test_format_includes_author(status):
    assert status['user']['screen_name'] in format(status)


@pytest.fixture
def session():
    key, secret = credentials()
    return twitter_session(key, secret)


@pytest.mark.parametrize('term', ('installfest', 'linuxdays'))
def test_search_results_contain_something(session, term):
    results = search(session, term)
    assert len(results) > 5
