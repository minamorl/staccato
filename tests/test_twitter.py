import pytest


def test_update_status(api):
    res = api.statuses_update(status="@tos status")
    api.statuses_destroy(res['id'])


def test_account_verify_credentials(api, conf):
    assert api.account_verify_credentials()['screen_name'] == conf["SCREEN_NAME"]


def test_get_followers(api, conf):
    print(api.get_followers(screen_name=conf["SCREEN_NAME"]))


def test_get_followings(api, conf):
    print(api.get_followings(screen_name=conf["SCREEN_NAME"]))

