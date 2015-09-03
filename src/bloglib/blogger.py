from __future__ import print_function
import sys
import requests
from oauth2client import client
from googleapiclient import sample_tools


def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(argv, 'blogger', 'v3', __doc__, __file__, scope='https://www.googleapis.com/auth/blogger')
    print(argv)
    url = "https://www.googleapis.com/blogger/v3/blogs/2695162313979547061/posts/"
    parameters = {'title':'XYZ'}
    r = requests.get(url, params=parameters)


