__author__ = 'spandey2405'
import sys ,os
BASE_DIR = os.path.realpath(sys.argv[0]).split('/conf')[0]
sys.path.append(BASE_DIR)


log_dir = BASE_DIR + "/log/"
db_dir = BASE_DIR + "/database/"

conf =  {
    "log":{
        "Debug" : log_dir + "debug.log",
        "Error" : log_dir + "error.log"   ,
        "Warning": log_dir + "warning.log",
        "Critical":log_dir + "critical.log"
          },
    "database":{
        "fb_page" : db_dir + "fb_page.db",
        "blogger" : db_dir + "blog.db"

    }

        }

