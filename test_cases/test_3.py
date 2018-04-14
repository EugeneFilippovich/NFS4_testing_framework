from main_files import *


class TestCase3(Commands):
    # TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase3.logger.info(Constants.INFO_RENAME + Constants.INFO_READ_WRITE_PROPERTY)

        step_1 = Commands.ssh_connect_to_server(Constants.SERVER_NAME, Constants.SERVER_IP, Constants.TOUCH_COMMAND +
                                                Constants.HOST_SHARE_PATH +
                                                Constants.FILE_NAME)
        Assertion.assert_ssh_to_server(step_1, TestCase3, 1)

        step_2 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step_2, TestCase3, 2)
        Assertion.assert_working_dir(TestCase3)

        step_3 = Commands.remove_file(Constants.FILE_NAME)
        Assertion.assert_remove_file(step_3, TestCase3, 3)
        Assertion.assert_list_of_files(TestCase3)
