from main_files import *


class TestCase1(Commands):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase1.logger.info(Constants.INFO_CREATE + Constants.INFO_READ_ONLY_PROPERTY)

        step_1 = Commands.change_folder(path=Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step=step_1, class_name=TestCase1, steps_quantity=1)
        Assertion.assert_working_dir(TestCase1)

        step_2 = Commands.touch_file(file_name=Constants.FILE_NAME)
        Assertion.assert_touch_file(step=step_2, class_name=TestCase1, steps_quantity=2)

        step_3 = Commands.cat_file(file_name=Constants.FILE_NAME)
        Assertion.assert_cat_file(step=step_3, class_name=TestCase1, steps_quantity=3)
        Assertion.assert_list_of_files(TestCase1)
