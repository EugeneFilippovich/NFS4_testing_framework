from main_files import *


class TestCase4(main_cases.MainCases):
    #TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(unique_logger.CustomMadeLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(unique_logger.CustomMadeLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase4.logger.info(constants.Constants.INFO_RENAME + constants.Constants.INFO_READ_WRITE_PROPERTY)
        step_1 = main_cases.MainCases.ssh_connect_to_server(constants.Constants.SERVER_NAME, constants.Constants.SERVER_IP,
                                                constants.Constants.TOUCH_COMMAND + constants.Constants.HOST_SHARE_PATH +
                                                constants.Constants.FILE_NAME)
        assertion.Assertion.assert_ssh_to_server(step_1, TestCase4, 1)

        step_2 = main_cases.MainCases.make_directory(constants.Constants.DIRECTORY_PATH_STATEMENTS + constants.Constants.DIRECTORY_NAME)
        assertion.Assertion.assert_make_dir(step_2, TestCase4, 2)

        step_3 = main_cases.MainCases.change_folder(constants.Constants.CLIENT_SHARE_PATH)
        assertion.Assertion.assert_change_folder(step_3, TestCase4, 3)
        assertion.Assertion.assert_working_dir(TestCase4)

        step_4 = main_cases.MainCases.copy_file(constants.Constants.FILE_NAME, constants.Constants.TEST_FOLDER_PATH
                                              + constants.Constants.TEST_FOLDER_PATH)
        assertion.Assertion.assert_copy_file(step_4, TestCase4, 4)

        step_5 = main_cases.MainCases.cat_file(constants.Constants.TEST_FOLDER_PATH + constants.Constants.TEST_FOLDER_PATH +
                                               '/' + constants.Constants.FILE_NAME)
        assertion.Assertion.assert_cat_file(step_5, TestCase4, 5)
        assertion.Assertion.assert_list_of_files(TestCase4)