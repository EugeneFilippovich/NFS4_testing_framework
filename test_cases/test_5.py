from main_files import *


class TestCase5(main_cases.MainCases):
    #TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(unique_logger.CustomMadeLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(unique_logger.CustomMadeLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase5.logger.info(constants.Constants.INFO_COPY + constants.Constants.INFO_READ_WRITE_PROPERTY)
        step_1 = main_cases.MainCases.make_directory(constants.Constants.TEST_FOLDER_PATH)
        assertion.Assertion.assert_make_dir(step_1, TestCase5, 1)

        step_2 = main_cases.MainCases.change_folder(constants.Constants.TEST_FOLDER_PATH + constants.Constants.DIRECTORY_NAME)
        assertion.Assertion.assert_change_folder(step_2, TestCase5, 2)
        assertion.Assertion.assert_working_dir(TestCase5)

        step_3 = main_cases.MainCases.touch_file(constants.Constants.FILE_NAME)
        assertion.Assertion.assert_touch_file(step_3, TestCase5, 3)

        step_4 = main_cases.MainCases.move_file(constants.Constants.FILE_NAME, constants.Constants.CLIENT_SHARE_PATH)
        assertion.Assertion.assert_move_file(step_4, TestCase5, 4)
        assertion.Assertion.assert_list_of_files(TestCase5)

        step_5 = main_cases.MainCases.change_folder(constants.Constants.CLIENT_SHARE_PATH)
        assertion.Assertion.assert_change_folder(step_5, TestCase5, 5)
        assertion.Assertion.assert_working_dir(TestCase5)
        assertion.Assertion.assert_list_of_files(TestCase5)


