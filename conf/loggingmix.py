__author__ = 'spandey2405'
import logging
import conf

def DEBUG(log):
    logging.basicConfig(filename=conf["log"]["Debug"],level=logging.DEBUG)
    logging.debug(log)

def WARNING(log):
    logging.basicConfig(filename=conf["log"]["Warning"],level=logging.WARNING)
    logging.debug(log)


def ERROR(log):
    logging.basicConfig(filename=conf["log"]["Error"],level=logging.ERROR)
    logging.debug(log)

def CRITICAL(log):
    logging.basicConfig(filename=conf["log"]["Critical"],level=logging.CRITICAL)
    logging.debug(log)
