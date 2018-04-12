from main_files import *


class TestCase8(main_cases.MainCases):
    #TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(unique_logger.CustomMadeLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(unique_logger.CustomMadeLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase8.logger.info(constants.Constants.INFO_REMOVE + constants.Constants.INFO_READ_ONLY_PROPERTY)
        step_1 = main_cases.MainCases.ssh_connect_to_server(constants.Constants.SERVER_NAME, constants.Constants.SERVER_IP,
                                                constants.Constants.TOUCH_COMMAND + constants.Constants.HOST_SHARE_PATH +
                                                constants.Constants.FILE_NAME)
        assertion.Assertion.assert_ssh_to_server(step_1, TestCase8, 1)

        step_2 = main_cases.MainCases.change_folder(constants.Constants.CLIENT_SHARE_PATH)
        assertion.Assertion.assert_change_folder(step_2, TestCase8, 2)
        assertion.Assertion.assert_working_dir(TestCase8)

        step_3 = main_cases.MainCases.remove_file(constants.Constants.FILE_NAME)
        assertion.Assertion.assert_remove_file(step_3, TestCase8, 3)
        assertion.Assertion.assert_list_of_files(TestCase8)