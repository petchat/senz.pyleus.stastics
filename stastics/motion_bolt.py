import json
from dao import *
from pyleus.storm import SimpleBolt

log = logging.getLogger("stastics_logger.first_bolt")


class MotionBolt(SimpleBolt):
    def process_tuple(self, tup):
        for i, v in enumerate(tup.values):
            obj = json.loads(v)
            user_id = obj.get('user_id')
            motion = obj.get('motionProb') or {}
            timestamp = obj.get('timestamp') or None
            push_motion(user_id, timestamp=timestamp, motion=motion)


if __name__ == '__main__':
    MotionBolt().run()

