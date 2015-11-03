import pytest
import os
import itertools


def test_account_verify_credentials(api):
    assert api.account_verify_credentials()['screen_name'] == os.environ["SCREEN_NAME"]


def test_get_followers(api):
    api.followers_ids(screen_name=os.environ["SCREEN_NAME"])


def test_get_followings(api):
    api.friends_ids(screen_name=os.environ["SCREEN_NAME"])


def test_user_stream(api):
    for parsed in itertools.islice(api.user_stream(), 10):
        pass
