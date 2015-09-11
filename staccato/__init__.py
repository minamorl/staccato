import staccato.twitter

def startup(session=None):
    return staccato.twitter.Twitter(session)
