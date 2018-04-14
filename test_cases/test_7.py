from main_files import *


class TestCase7(Commands):
    # TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase7.logger.info(Constants.INFO_MOVE + Constants.INFO_READ_ONLY_PROPERTY)

        step_1 = Commands.change_folder(Constants.TEST_FOLDER_PATH + Constants.TEST_DIRECTORY_NAME)
        Assertion.assert_make_dir(step_1, TestCase7, 1)

        step_2 = Commands.change_folder(Constants.TEST_FOLDER_PATH + Constants.TEST_DIRECTORY_NAME)
        Assertion.assert_change_folder(step_2, TestCase7, 2)
        Assertion.assert_working_dir(TestCase7)

        step_3 = Commands.touch_file(Constants.FILE_NAME)
        Assertion.assert_touch_file(step_3, TestCase7, 3)

        step_4 = Commands.move_file(Constants.FILE_NAME, Constants.CLIENT_SHARE_PATH)
        Assertion.assert_move_file(step_4, TestCase7, 4)
        Assertion.assert_list_of_files(TestCase7)

        step_5 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step_5, TestCase7, 5)
        Assertion.assert_working_dir(TestCase7)
        Assertion.assert_list_of_files(TestCase7)
