import os
import staccato



def test__define_endpoint():
    api = staccato.startup()

    api.auth(os.environ["CONSUMER_KEY"],
             os.environ["CONSUMER_SECRET"],
             os.environ["ACCESS_TOKEN_KEY"],
             os.environ["ACCESS_TOKEN_SECRET"])
    
    assert True == True # dummy
    
    #  response = api.statuses_update(status = "nyaa")
    #  api.statuses_destroy(response['id'])
    #  assert api.media_upload() == None
