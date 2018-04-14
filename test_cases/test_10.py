from main_files import *


class TestCase10(Commands):
    # TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase10.logger.info(Constants.INFO_WRITE_DATA + Constants.INFO_READ_ONLY_PROPERTY)

        step_1 = Commands.ssh_connect_to_server(Constants.SERVER_NAME, Constants.SERVER_IP,
                                                Constants.TOUCH_COMMAND + Constants.HOST_SHARE_PATH +
                                                Constants.FILE_NAME)
        Assertion.assert_ssh_to_server(step_1, TestCase10, 1)

        step_2 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step_2, TestCase10, 2)
        Assertion.assert_working_dir(TestCase10)

        step_3 = Commands.write_file(Constants.FILE_NAME, Constants.TEST_STRING)
        Assertion.assert_write_into_file(step_3, TestCase10, 3)
        Assertion.assert_read_file(TestCase10, Constants.FILE_NAME)
