from main_files import *


class TestCase6(main_cases.MainCases):
    #TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(unique_logger.CustomMadeLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(unique_logger.CustomMadeLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase6.logger.info(constants.Constants.INFO_EXECUTE + constants.Constants.INFO_READ_WRITE_PROPERTY)
        step_1 = main_cases.MainCases.change_folder(constants.Constants.CLIENT_SHARE_PATH)
        assertion.Assertion.assert_change_folder(step_1, TestCase6, 1)
        assertion.Assertion.assert_working_dir(TestCase6)

        step_2 = main_cases.MainCases.touch_file(constants.Constants.FILE_NAME)
        assertion.Assertion.assert_touch_file(step_2, TestCase6, 2)
        assertion.Assertion.assert_list_of_files(TestCase6)

        step_3 = main_cases.MainCases.write_file(constants.Constants.FILE_NAME, constants.Constants.TEST_STRING)
        assertion.Assertion.assert_write_into_file(step_3, TestCase6, 3)
        assertion.Assertion.assert_read_file(TestCase6, constants.Constants.FILE_NAME)

        step_4 = main_cases.MainCases.execute_script(constants.Constants.FILE_NAME)
        assertion.Assertion.assert_run_script(step_4, TestCase6, 4)

    