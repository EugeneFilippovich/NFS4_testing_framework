from main_files import *


class TestCase1(Commands):
    # TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase1.logger.info(Constants.INFO_CREATE + Constants.INFO_READ_ONLY_PROPERTY)

        step_1 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step_1, TestCase1, 1)
        Assertion.assert_working_dir(TestCase1)

        step_2 = Commands.touch_file(Constants.FILE_NAME)
        Assertion.assert_touch_file(step_2, TestCase1, 2)

        step_3 = Commands.cat_file(Constants.FILE_NAME)
        Assertion.assert_cat_file(step_3, TestCase1, 3)
        Assertion.assert_list_of_files(TestCase1)
