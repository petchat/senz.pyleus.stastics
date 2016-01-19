import logging
# from pymongo import MongoClient
#
# RefinedLog = MongoClient('mongodb://senzhub:Senz2everyone@119.254.111.40/RefinedLog')
# forTest = RefinedLog.get_default_database().ForTest
log = logging.getLogger("stastics_logger.first_spout")


def push_motion(uid, **kwargs):
    for k, v in kwargs.items():
        log.info("[%r] %r: %r", uid, k, v)


def push_event(uid, **kwargs):
    for k, v in kwargs.items():
        log.info("[%r] %r: %r", uid, k, v)


def push_location(uid, **kwargs):
    for k, v in kwargs.items():
        log.info("[%r] %r: %r", uid, k, v)
