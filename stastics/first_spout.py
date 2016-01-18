import logging

from pyleus.storm import Spout

log = logging.getLogger("stastics_logging.first_spout")


class LineSpout(Spout):
    # OUTPUT_FIELDS = ['timestamp', 'added']

    def next_tuple(self, tup):
        self.emit(tup)
        log.info("Emitted: %r", tup)


if __name__ == '__main__':
    LineSpout().run()
