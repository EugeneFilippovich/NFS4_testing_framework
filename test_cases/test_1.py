from main_files import *


class TestCase1(main_cases.MainCases):
    #TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(unique_logger.CustomMadeLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(unique_logger.CustomMadeLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase1.logger.info(constants.Constants.INFO_CREATE + constants.Constants.INFO_READ_ONLY_PROPERTY)
        step_1 = main_cases.MainCases.change_folder(constants.Constants.CLIENT_SHARE_PATH)
        assertion.Assertion.assert_change_folder(step_1, TestCase1, 1)
        assertion.Assertion.assert_working_dir(TestCase1)

        step_2 = main_cases.MainCases.touch_file(constants.Constants.FILE_NAME)
        assertion.Assertion.assert_touch_file(step_2, TestCase1, 2)

        step_3 = main_cases.MainCases.cat_file(constants.Constants.FILE_NAME)
        assertion.Assertion.assert_cat_file(step_3, TestCase1, 3)
        assertion.Assertion.assert_list_of_files(TestCase1)

