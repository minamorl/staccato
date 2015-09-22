import os
import pytest
import staccato


@pytest.fixture
def api():
    api = staccato.startup()
    api.auth(os.environ["CONSUMER_KEY"],
             os.environ["CONSUMER_SECRET"],
             os.environ["ACCESS_TOKEN_KEY"],
             os.environ["ACCESS_TOKEN_SECRET"])
    return api
