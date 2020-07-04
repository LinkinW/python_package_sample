import logging
import test_pack.pack_logging


def print_hello(s):
    for i in range(10):    
        logging.info('Hello %s %d !' % (s, i))
