import sys
sys.path.insert(0, '..')

from test_pack import *

if __name__ == '__main__':
	pack_logging.set_log('WARN')
	print_hello('hehe')