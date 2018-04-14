from main_files import *


class TestCase5(Commands):
    #TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase5.logger.info(Constants.INFO_COPY + Constants.INFO_READ_WRITE_PROPERTY)

        step_1 = Commands.make_directory(Constants.TEST_FOLDER_PATH)
        Assertion.assert_make_dir(step_1, TestCase5, 1)

        step_2 = Commands.change_folder(Constants.TEST_FOLDER_PATH + Constants.TEST_DIRECTORY_NAME)
        Assertion.assert_change_folder(step_2, TestCase5, 2)
        Assertion.assert_working_dir(TestCase5)

        step_3 = Commands.touch_file(Constants.FILE_NAME)
        Assertion.assert_touch_file(step_3, TestCase5, 3)

        step_4 = Commands.move_file(Constants.FILE_NAME, Constants.CLIENT_SHARE_PATH)
        Assertion.assert_move_file(step_4, TestCase5, 4)
        Assertion.assert_list_of_files(TestCase5)

        step_5 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step_5, TestCase5, 5)
        Assertion.assert_working_dir(TestCase5)
        Assertion.assert_list_of_files(TestCase5)


