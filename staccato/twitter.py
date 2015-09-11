from requests_oauthlib import OAuth1Session
from json import JSONDecoder
from staccato import utils


class Twitter():
    API = "https://api.twitter.com/1.1/"

    def __init__(self, session=None):
        self.session = session

    def auth(self, consumer_key, consumer_secret, access_token_key, access_token_secret):

        session = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token_key,
            resource_owner_secret=access_token_secret)

        self.session=session

    def request(self, method='get', endpoint='', **kwargs):

        def _parsed(s):
            try:
                return JSONDecoder().decode(s)
            except:
                return s

        if self.session is None:
            raise TwitterAuthException()

        _url=Twitter.API + endpoint
        parsed=_parsed(self.session.request(method, _url, **kwargs).text)

        return parsed

    def get_followers(self, screen_name, count=0):
        return self.request("get", "followers/ids.json", params={"screen_name": screen_name, "count": count})

    def get_followings(self, screen_name, count=0):
        return self.request("get", "friends/ids.json", params={"screen_name": screen_name, "count": count})

    def lookup(self, user_ids):
        result=[]
        for ids in utils.chunk(user_ids, 100):
            r=self.request("get", "users/lookup.json", params={"user_id": ','.join(ids)})
            result.extend(r)
        return result

    def remove_user(self, user_id):
        return self.request("post", "friendships/destroy.json", params={"user_id": user_id})


class TwitterAuthException(Exception):
    pass
