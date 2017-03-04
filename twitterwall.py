import base64
import configparser
import os
import time
import sys

import click
import requests


def twitter_session(api_key, api_secret):
    session = requests.Session()
    secret = '{}:{}'.format(api_key, api_secret)
    secret64 = base64.b64encode(secret.encode('ascii')).decode('ascii')

    headers = {
        'Authorization': 'Basic {}'.format(secret64),
        'Host': 'api.twitter.com',
    }

    r = session.post('https://api.twitter.com/oauth2/token',
                     headers=headers,
                     data={'grant_type': 'client_credentials'})
    r.raise_for_status()

    bearer_token = r.json()['access_token']

    def bearer_auth(req):
        req.headers['Authorization'] = 'Bearer ' + bearer_token
        return req

    session.auth = bearer_auth
    return session


def search(session, q, since_id=1):
    r = session.get('https://api.twitter.com/1.1/search/tweets.json',
                    params={'q': q, 'since_id': since_id})
    r.raise_for_status()
    return r.json()['statuses']


def format_entity(entity):
    if entity['type'] == 'user_mentions':
        return click.style(
            '@' + entity['screen_name'],
            fg='green',
            bold=True
        )
    if entity['type'] == 'hashtags':
        return click.style(
            '#' + entity['text'],
            fg='blue',
            bold=True
        )
    if entity['type'] == 'symbols':
        return click.style(
            '$' + entity['text'],
            fg='yellow',
            bold=True
        )
    if entity['type'] == 'urls':
        return click.style(
            entity['expanded_url'],
            fg='red'
        )


def entities(status):
    TYPES = ['hashtags', 'symbols', 'urls', 'user_mentions']
    ents = {}
    for t in TYPES:
        for e in status['entities'][t]:
            e['type'] = t
            ents[e['indices'][0]] = e

    text = status['text']

    for i in reversed(range(len(status['text']))):
        try:
            end = ents[i]['indices'][1]
            text = text[:i] + format_entity(ents[i]) + text[end:]
        except KeyError:
            pass
    return text


def format(status):
    author = click.style(
        status['user']['screen_name'],
        fg='magenta',
        bold=True
    )
    text = entities(status)
    return '{}: {}'.format(author, text)


def credentials(inipath=os.path.expanduser('~/.twitter.ini')):
    config = configparser.ConfigParser()
    config.read(inipath)
    key = config['auth']['key']
    secret = config['auth']['secret']
    return key, secret


@click.command()
@click.option('--sleep', default=3, help='Sleep duration between API calls.')
@click.option('--query', prompt='Search', help='What to search for.')
def main(sleep, query):
    """Twitter wall for console"""
    key, secret = credentials()

    try:
        session = twitter_session(key, secret)
    except Exception as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    last_id = 1

    while True:
        try:
            statuses = search(session, query, last_id)
            if statuses:
                last_id = statuses[0]['id']
            for status in reversed(statuses):
                click.echo(format(status))
            time.sleep(sleep)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(str(e), file=sys.stderr)


if __name__ == '__main__':
    main()
