import os
import pytest
from configparser import ConfigParser
from staccato.twitter import Twitter, TwitterAuthException


@pytest.fixture
def conf():
    conf = ConfigParser()
    conf.read(os.path.expanduser("~/.staccato.conf"))
    conf = conf['OAuth1Settings']
    return conf


@pytest.fixture
def api():
    conf = ConfigParser()
    conf.read(os.path.expanduser("~/.staccato.conf"))
    conf = conf['OAuth1Settings']
    api = Twitter()
    api.auth(conf["CONSUMER_KEY"],
             conf["CONSUMER_SECRET"],
             conf["ACCESS_TOKEN_KEY"],
             conf["ACCESS_TOKEN_SECRET"])
    return api
