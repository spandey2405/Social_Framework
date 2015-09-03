__author__ = 'spandey2405'

import anydbm
from conf import conf



def db_entery(db_type, data):
    db = anydbm.open(conf["database"][db_type], 'c')
    for key in data:
        db[key] = data[key]

def get_from_db(db_type):
    data ={}
    db = anydbm.open(conf["database"][db_type], 'c')
    for key, value in db.iteritems():
        data[key]=value
    return data


# log_debug("Error","Error: Some Error Message")

# db_entery("blogger",data)
# get_from_db("blogger")