from main_files import *


class TestCase5(Commands):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase5.logger.info(Constants.INFO_COPY + Constants.INFO_READ_WRITE_PROPERTY)

        step_1 = Commands.make_directory(folder_name=Constants.TEST_FOLDER_PATH)
        Assertion.assert_make_dir(step=step_1, class_name=TestCase5, steps_quantity=1)

        step_2 = Commands.change_folder(Constants.TEST_FOLDER_PATH + Constants.TEST_DIRECTORY_NAME)
        Assertion.assert_change_folder(step=step_2, class_name=TestCase5, steps_quantity=2)
        Assertion.assert_working_dir(TestCase5)

        step_3 = Commands.touch_file(Constants.FILE_NAME)
        Assertion.assert_touch_file(step=step_3, class_name=TestCase5, steps_quantity=3)

        step_4 = Commands.move_file(Constants.FILE_NAME, Constants.CLIENT_SHARE_PATH)
        Assertion.assert_move_file(step=step_4, class_name=TestCase5, steps_quantity=4)
        Assertion.assert_list_of_files(TestCase5)

        step_5 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step=step_5, class_name=TestCase5, steps_quantity=5)
        Assertion.assert_working_dir(TestCase5)
        Assertion.assert_list_of_files(TestCase5)


