__author__ = 'spandey2405'
from Social_Handler.src import handler
import anydbm

access_token = "gfaskjdhakjldhflkadshgkjasdhglkjasdhglkashdlgkasdhl"

while True:
    parameters = handler.read_post(page_id="funnymiku.in", access_token=access_token, limit=1,parameters=parameters)
    raw_input()

def post_on_blog(blog_id,fb_page_id, access_token):

    return None

