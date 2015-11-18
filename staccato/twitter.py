from requests_oauthlib import OAuth1Session
from json import JSONDecoder
from staccato import utils

def __define_endpoint(method, endpoint, id=False):
    if id:
        def fn(self, id, **kwargs):
            url = "{}/{}.json".format(endpoint, id)
            return self.request(method, url, params=kwargs)
        return fn
    else:
        def fn(self, **kwargs):
            url = "{}.json".format(endpoint)
            return self.request(method, url, params=kwargs)
        return fn


class Twitter():
    API = "https://api.twitter.com/1.1/"

    def __init__(self, session=None):
        self.session = session

    def auth(self, consumer_key, consumer_secret, access_token_key=None, access_token_secret=None):

        session = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token_key,
            resource_owner_secret=access_token_secret)

        self.session = session

    def generate_auth_url(self):
        request_token_url = 'https://api.twitter.com/oauth/request_token'
        base_authorization_url = 'https://api.twitter.com/oauth/authorize'
        fetch_response = self.session.fetch_request_token(request_token_url)
        return self.session.authorization_url(base_authorization_url)

    def pin_auth(self, pin):
        access_token_url = 'https://api.twitter.com/oauth/access_token'
        oauth_response = self.session.fetch_access_token(access_token_url, verifier=pin)
        return oauth_response

    def request(self, method='get', endpoint='', **kwargs):

        def _parsed(s):
            try:
                return JSONDecoder().decode(s)
            except:
                return s

        if self.session is None:
            raise TwitterAuthException()

        _url = Twitter.API + endpoint
        parsed = _parsed(self.session.request(method, _url, **kwargs).text)

        return parsed

    def lookup(self, user_ids):
        result = []
        for ids in utils.chunk(user_ids, 100):
            r = self.request("get", "users/lookup.json", params={"user_id": ','.join(ids)})
            result.extend(r)
        return result

    statuses_mentions_timeline = __define_endpoint("get", "statuses/mentions_timeline")
    statuses_user_timeline = __define_endpoint("get", "statuses/user_timeline")
    statuses_home_timeline = __define_endpoint("get", "statuses/home_timeline")
    statuses_retweets_of_me = __define_endpoint("get", "statuses/retweets_of_me")
    statuses_retweets = __define_endpoint("get", "statuses/retweets", True)
    statuses_show = __define_endpoint("get", "statuses/show", True)
    statuses_destroy = __define_endpoint("post", "statuses/destroy", True)
    statuses_update = __define_endpoint("post", "statuses/update")
    statuses_retweet = __define_endpoint("post", "statuses/retweet")
    statuses_update_with_media = __define_endpoint("post", "statuses/update_with_media")
    statuses_oembed = __define_endpoint("get", "statuses/oembed")
    statuses_retweeters_ids = __define_endpoint("get", "statuses/retweeters/ids")
    statuses_lookup = __define_endpoint("get", "statuses/lookup")
    media_upload = __define_endpoint("post", "media/upload")
    direct_messages_sent = __define_endpoint("get", "direct_messages/sent")
    direct_messages_show = __define_endpoint("get", "direct_messages/show")
    search_tweets = __define_endpoint("get", "search/tweets")
    direct_messages = __define_endpoint("get", "direct_messages")
    direct_messages_destroy = __define_endpoint("post", "direct_messages/destroy")
    direct_messages_new = __define_endpoint("post", "direct_messages/new")
    friendships_no_retweets_ids = __define_endpoint("get", "friendships/no_retweets/ids")
    friends_ids = __define_endpoint("get", "friends/ids")
    followers_ids = __define_endpoint("get", "followers/ids")
    friendships_incoming = __define_endpoint("get", "friendships/incoming")
    friendships_outgoing = __define_endpoint("get", "friendships/outgoing")
    friendships_create = __define_endpoint("post", "friendships/create")
    friendships_destroy = __define_endpoint("post", "friendships/destroy")
    friendships_update = __define_endpoint("post", "friendships/update")
    friendships_show = __define_endpoint("get", "friendships/show")
    friends_list = __define_endpoint("get", "friends/list")
    followers_list = __define_endpoint("get", "followers/list")
    friendships_lookup = __define_endpoint("get", "friendships/lookup")
    account_settings = __define_endpoint("get", "account/settings")
    account_verify_credentials = __define_endpoint("get", "account/verify_credentials")
    account_settings = __define_endpoint("post", "account/settings")
    account_update_delivery_device = __define_endpoint("post", "account/update_delivery_device")
    account_update_profile = __define_endpoint("post", "account/update_profile")
    account_update_profile_background_image = __define_endpoint("post", "account/update_profile_background_image")
    account_update_profile_image = __define_endpoint("post", "account/update_profile_image")
    blocks_list = __define_endpoint("get", "blocks/list")
    blocks_ids = __define_endpoint("get", "blocks/ids")
    blocks_create = __define_endpoint("post", "blocks/create")
    blocks_destroy = __define_endpoint("post", "blocks/destroy")
    users_lookup = __define_endpoint("get", "users/lookup")
    users_show = __define_endpoint("get", "users/show")
    users_search = __define_endpoint("get", "users/search")
    account_remove_profile_banner = __define_endpoint("post", "account/remove_profile_banner")
    account_update_profile_banner = __define_endpoint("post", "account/update_profile_banner")
    users_profile_banner = __define_endpoint("get", "users/profile_banner")
    favorites_list = __define_endpoint("get", "favorites/list")
    favorites_destroy = __define_endpoint("post", "favorites/destroy")
    favorites_create = __define_endpoint("post", "favorites/create")
    lists_list = __define_endpoint("get", "lists/list")
    lists_statuses = __define_endpoint("get", "lists/statuses")
    lists_members_destroy = __define_endpoint("post", "lists/members/destroy")
    lists_memberships = __define_endpoint("get", "lists/memberships")
    lists_subscribers = __define_endpoint("get", "lists/subscribers")
    lists_subscribers_create = __define_endpoint("post", "lists/subscribers/create")
    lists_subscribers_show = __define_endpoint("get", "lists/subscribers/show")
    lists_subscribers_destroy = __define_endpoint("post", "lists/subscribers/destroy")
    lists_members_create_all = __define_endpoint("post", "lists/members/create_all")
    lists_members_show = __define_endpoint("get", "lists/members/show")
    lists_members = __define_endpoint("get", "lists/members")
    lists_members_create = __define_endpoint("post", "lists/members/create")
    lists_destroy = __define_endpoint("post", "lists/destroy")
    lists_update = __define_endpoint("post", "lists/update")
    lists_create = __define_endpoint("post", "lists/create")
    lists_show = __define_endpoint("get", "lists/show")
    lists_subscriptions = __define_endpoint("get", "lists/subscriptions")
    lists_members_destroy_all = __define_endpoint("post", "lists/members/destroy_all")
    lists_ownerships = __define_endpoint("get", "lists/ownerships")
    saved_searches_list = __define_endpoint("get", "saved_searches/list")
    saved_searches_show = __define_endpoint("get", "saved_searches/show", True)
    saved_searches_create = __define_endpoint("post", "saved_searches/create")
    saved_searches_destroy = __define_endpoint("post", "saved_searches/destroy", True)
    trends_place = __define_endpoint("get", "trends/place")
    trends_available = __define_endpoint("get", "trends/available")
    application_rate_limit_status = __define_endpoint("get", "application/rate_limit_status")
    help_configuration = __define_endpoint("get", "help/configuration")
    help_languages = __define_endpoint("get", "help/languages")
    help_privacy = __define_endpoint("get", "help/privacy")
    help_tos = __define_endpoint("get", "help/tos")
    trends_closest = __define_endpoint("get", "trends/closest")
    users_report_spam = __define_endpoint("post", "users/report_spam")
    geo_id_place_id = __define_endpoint("get", "geo/id", True)
    geo_reverse_geocode = __define_endpoint("get", "geo/reverse_geocode")
    geo_search = __define_endpoint("get", "geo/search")
    geo_place = __define_endpoint("post", "geo/place")

    def user_stream(self):
        r = self.session.get('https://userstream.twitter.com/1.1/user.json', stream=True)
        decoder = JSONDecoder()
        for line in r.iter_lines():
            if line: 
                yield decoder.decode(line.decode())


class TwitterAuthException(Exception):
    pass
