import logging

from pyleus.storm import Spout

log = logging.getLogger("stastics_logger.first_spout")


class LineSpout(Spout):
    def next_tuple(self, tup):
        self.emit(tup)


if __name__ == '__main__':
    LineSpout().run()
