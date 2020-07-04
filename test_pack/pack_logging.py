import logging

logging.basicConfig(level=logging.WARN,
	format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

def set_log(log_level='WARN'):

	if log_level == 'DEBUG':
		print('DEBUG mode on')
		logging.root.setLevel(logging.DEBUG)

	else:
		logging.root.setLevel(logging.WARN)