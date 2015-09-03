__author__ = 'spandey2405'

import requests

def post_status(page_id, access_token, message, scheduled_publish_time = None):
    url = url = "https://graph.facebook.com/v2.4/" + page_id + "/feed"
    if scheduled_publish_time:
        parameters = {'access_token':access_token,'message':message, 'scheduled_publish_time':scheduled_publish_time, 'published':'false'}
    else:
        parameters = {'access_token':access_token,'message':message}
    r = requests.post(url, params=parameters)
    return r.json()

