import pytest

from twitterwall import format


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
