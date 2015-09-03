__author__ = 'spandey2405'
import fetch
import requests
import os,sys
def get_post(page_id,access_token,limit, parameters=None):
    data = fetch.get_data_json(page_id,access_token,limit, parameters=parameters)
    try:
        posts = data["data"]
    except:
        print data
        sys.exit(0)
    else:
        return posts

def next_page(page_id,access_token,limit, parameters=None):
    data = fetch.get_data_json(page_id,access_token,limit, parameters=parameters)
    parameters = {}
    next = data["paging"]["next"]
    parms = next.split("?")
    parms = parms[1].split("&")
    for param in parms:
        para = param.split("=")
        parameters[para[0]]=para[1]
    return parameters

def put_post(page_id, access_token, message, scheduled_publish_time = None):

    return None



