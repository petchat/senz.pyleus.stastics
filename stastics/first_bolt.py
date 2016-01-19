import json
from dao import *
from pymongo import MongoClient
from pyleus.storm import SimpleBolt

log = logging.getLogger("stastics_logger.first_bolt")
RefinedLog = MongoClient('mongodb://senzhub:Senz2everyone@119.254.111.40/RefinedLog')


class MotionBolt(SimpleBolt):
    def process_tuple(self, tup):
        for i, v in enumerate(tup.values):
            obj = json.loads(v)
            user_id = obj.get('user_id')
            motion = obj.get('motionProb') or {}
            timestamp = obj.get('timestamp') or None
            push_motion(user_id, timestamp=timestamp, motion=motion)
            log.info("[ %r ] Motion: %r", user_id, motion.items())


if __name__ == '__main__':
    MotionBolt().run()


# if __name__ == '__main__':
#     forTest = RefinedLog.get_default_database().ForTest
#     print forTest.count()
