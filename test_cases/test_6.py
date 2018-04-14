from main_files import *


class TestCase6(Commands):
    # TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase6.logger.info(Constants.INFO_EXECUTE + Constants.INFO_READ_WRITE_PROPERTY)

        step_1 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step_1, TestCase6, 1)
        Assertion.assert_working_dir(TestCase6)

        step_2 = Commands.touch_file(Constants.FILE_NAME)
        Assertion.assert_touch_file(step_2, TestCase6, 2)
        Assertion.assert_list_of_files(TestCase6)

        step_3 = Commands.write_file(Constants.FILE_NAME, Constants.TEST_STRING)
        Assertion.assert_write_into_file(step_3, TestCase6, 3)
        Assertion.assert_read_file(TestCase6, Constants.FILE_NAME)

        step_4 = Commands.execute_script(Constants.FILE_NAME)
        Assertion.assert_run_script(step_4, TestCase6, 4)
