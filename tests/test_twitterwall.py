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


def test_format_startswith_author(status):
    assert format(status).startswith(status['user']['screen_name'])
