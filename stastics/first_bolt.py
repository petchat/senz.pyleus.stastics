import json
import logging
import logging.config
from pymongo import MongoClient
from pyleus.storm import SimpleBolt

log = logging.getLogger("stastics_logging.first_bolt")
RefinedLog = MongoClient('mongodb://senzhub:Senz2everyone@119.254.111.40/RefinedLog')


class LoggerBolt(SimpleBolt):
    def process_tuple(self, tup):
        for i, v in enumerate(tup.values):
            obj = json.loads(v)
            motion = obj.get('motionProb') or {}
            user_id = obj.get('user_id')
            log.info("[ %r ] Motion: %r", user_id, motion.items())


# if __name__ == '__main__':
#     LoggerBolt().run()


if __name__ == '__main__':
    forTest = RefinedLog.get_default_database().ForTest
    print forTest.count()
