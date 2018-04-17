from main_files import *


class TestCase6(Commands):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase6.logger.info(Constants.INFO_EXECUTE + Constants.INFO_READ_WRITE_PROPERTY)

        step_1 = Commands.change_folder(path=Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step=step_1, class_name=TestCase6, steps_quantity=1)
        Assertion.assert_working_dir(TestCase6)

        step_2 = Commands.touch_file(file_name=Constants.FILE_NAME)
        Assertion.assert_touch_file(step=step_2, class_name=TestCase6, steps_quantity=2)
        Assertion.assert_list_of_files(TestCase6)

        step_3 = Commands.write_file(file_name=Constants.FILE_NAME, data=Constants.TEST_DATA_TO_WRITE)
        Assertion.assert_write_into_file(step=step_3, class_name=TestCase6, steps_quantity=3)
        Assertion.assert_read_file(TestCase6, Constants.FILE_NAME)

        step_4 = Commands.execute_script(script_name=Constants.FILE_NAME)
        Assertion.assert_run_script(step=step_4, class_name=TestCase6, steps_quantity=4)
