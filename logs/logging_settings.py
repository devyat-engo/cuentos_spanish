import logging

from lib import vars

formatter = logging.Formatter(fmt='%(asctime)s | %(name)s | %(levelname)s | %(message)s', datefmt='%d.%m.%Y | %H:%M:%S')


def setup_logger(name, log_file, level=logging.INFO):

    handler = logging.FileHandler(f'{vars.logs_location}{log_file}.log', mode="a+")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
