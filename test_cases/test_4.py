from main_files import *


class TestCase4(Commands):
    # TODO comment
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase4.logger.info(Constants.INFO_RENAME + Constants.INFO_READ_WRITE_PROPERTY)

        step_1 = Commands.ssh_connect_to_server(Constants.SERVER_NAME, Constants.SERVER_IP,
                                                Constants.TOUCH_COMMAND + Constants.HOST_SHARE_PATH +
                                                Constants.FILE_NAME)
        Assertion.assert_ssh_to_server(step_1, TestCase4, 1)

        step_2 = Commands.make_directory(Constants.DIRECTORY_PATH_STATEMENTS +
                                         Constants.TEST_DIRECTORY_NAME)
        Assertion.assert_make_dir(step_2, TestCase4, 2)

        step_3 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step_3, TestCase4, 3)
        Assertion.assert_working_dir(TestCase4)

        step_4 = Commands.copy_file(Constants.FILE_NAME, Constants.TEST_FOLDER_PATH
                                    + constants.Constants.TEST_FOLDER_PATH)
        Assertion.assert_copy_file(step_4, TestCase4, 4)

        step_5 = Commands.cat_file(Constants.TEST_FOLDER_PATH + Constants.TEST_FOLDER_PATH +
                                   '/' + Constants.FILE_NAME)
        Assertion.assert_cat_file(step_5, TestCase4, 5)
        Assertion.assert_list_of_files(TestCase4)
