import os
import pytest
from configparser import ConfigParser
import os
from staccato.twitter import Twitter, TwitterAuthException


def _conf():
    prefix = "STACCATO_"
    conf = {}
    keys = list(item for item in list(os.environ) if item.startswith(prefix))
    print(keys)
    
    for key in keys:
        conf[key.replace(prefix, "")] = os.environ[key]
    return conf

@pytest.fixture
def conf():
    return _conf()

@pytest.fixture
def api():
    conf = _conf()
    api = Twitter()
    api.auth(conf["CONSUMER_KEY"],
             conf["CONSUMER_SECRET"],
             conf["ACCESS_TOKEN_KEY"],
             conf["ACCESS_TOKEN_SECRET"])
    return api
