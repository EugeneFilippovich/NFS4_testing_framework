import logging

from main_files import main_cases

from main_files import constants as cons


class CustomMadeLogger(main_cases):
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    console_stdout = logging.StreamHandler()
    console_stdout.setLevel(logging.INFO)
    console_stdout.setFormatter(formatter)
    file_handler = logging.FileHandler(cons.Constants.LOGGER_PATH + '/logger.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
