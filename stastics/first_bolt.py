import json
import logging
import logging.config

from pyleus.storm import SimpleBolt

log = logging.getLogger("stastics_logging.first_bolt")


class LoggerBolt(SimpleBolt):

    def process_tuple(self, tup):
        for i, v in enumerate(tup.values):
            # log.info("[** %d **]Received: %r", i, v)
            obj = json.loads(v)
            motion = obj.get('motionProb') or {}
            log.info("Motion: %r", motion.items())


if __name__ == '__main__':
    LoggerBolt().run()
