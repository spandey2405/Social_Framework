__author__ = 'spandey2405'
import os
from fblib import helper
from fblib import post_status
import time as TIME

access_token = "CAAVAZCza33C4BALedJLUxRad2JSGf6dTNPStGKCRXZBM6xUiZAT6uKts21O6S07ZC4ZB9ISlZA7yj4UfEnUenYDBgwFwUx7zrBMeR8eBfFZAU2VtsToq1qdZBdQOT1PaMnrChCtW36aJtqHZAMLuSCnbNEZCDvztbZAUe8ZBplvrqoKjcaYAxOpTPrQJGuPZADuzFQ21a3DVnsG2u6gZDZD"
parameters = None
message = None

def read_post(page_id, access_token,limit,parameters=None):
    os.system("clear")
    posts = helper.get_post(page_id,access_token,limit, parameters=parameters)
    for post in posts:
        try:
            print(post["message"])
        except:
            pass
    parameters = helper.next_page(page_id, access_token, limit, parameters=parameters)
    return parameters

def get_schedule_time():
    schedule_time = raw_input("Input Time_Stamp | hrs.min")
    schedule_time = schedule_time.split(".")
    add_time = (int(schedule_time[0])*60 + int(schedule_time[1]))*60
    time_sh = int(TIME.time() + add_time)
    return time_sh

def schedule_post(my_page_id, copy_page_id, access_token):
    choice = "y"
    parameters = None
    while (choice != "n"):
        os.system("clear")
        posts = helper.get_post(copy_page_id,access_token,limit=1, parameters=parameters)
        for post in posts:
            try:
                message = post["message"]
                print(post["message"])
                choice_post = raw_input("\n\nPress Enter To post .... \nPress x to see next post\nCtrl + Z to Exit")
                if choice_post !="x":
                    time_sh = get_schedule_time()
                    print post_status.post_status(page_id=my_page_id, access_token=access_token, message=message, scheduled_publish_time=time_sh)
            except Exception as e:
                pass
        parameters = helper.next_page(copy_page_id, access_token, limit=1, parameters=parameters)

schedule_post(my_page_id="funnymiku.in", copy_page_id="Fny.Kings", access_token=access_token)





