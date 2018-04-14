from main_files import *


class TestCase8(Commands):
    # TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase8.logger.info(Constants.INFO_REMOVE + Constants.INFO_READ_ONLY_PROPERTY)

        step_1 = Commands.ssh_connect_to_server(Constants.SERVER_NAME, Constants.SERVER_IP,
                                                Constants.TOUCH_COMMAND + Constants.HOST_SHARE_PATH +
                                                Constants.FILE_NAME)
        Assertion.assert_ssh_to_server(step_1, TestCase8, 1)

        step_2 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step_2, TestCase8, 2)
        Assertion.assert_working_dir(TestCase8)

        step_3 = Commands.remove_file(Constants.FILE_NAME)
        Assertion.assert_remove_file(step_3, TestCase8, 3)
        Assertion.assert_list_of_files(TestCase8)
