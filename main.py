import logging

import comm.highway

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.TRACE)
ch.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.TRACE)
logger.addHandler(ch)


