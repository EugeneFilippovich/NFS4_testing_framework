from main_files import *


class TestCase4(Commands):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase4.logger.info(Constants.INFO_RENAME + Constants.INFO_READ_WRITE_PROPERTY)

        step_1 = Commands.ssh_connect_to_server(host_name=Constants.HOST_USER_NAME, host_ip=Constants.HOST_IP,
                                                command_to_execute=Constants.TOUCH_COMMAND + Constants.HOST_SHARE_PATH +
                                                Constants.FILE_NAME)
        Assertion.assert_ssh_to_server(step=step_1, class_name=TestCase4, steps_quantity=1)

        step_2 = Commands.make_directory(folder_name=Constants.DIRECTORY_PATH_STATEMENTS +
                                         Constants.TEST_DIRECTORY_NAME)
        Assertion.assert_make_dir(step=step_2, class_name=TestCase4, steps_quantity=2)

        step_3 = Commands.change_folder(path=Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step=step_3, class_name=TestCase4, steps_quantity=3)
        Assertion.assert_working_dir(TestCase4)

        step_4 = Commands.copy_file(file_name=Constants.FILE_NAME, destination_path=Constants.TEST_FOLDER_PATH
                                    + constants.Constants.TEST_FOLDER_PATH)
        Assertion.assert_copy_file(step=step_4, class_name=TestCase4, steps_quantity=4)

        step_5 = Commands.cat_file(file_name=Constants.TEST_FOLDER_PATH + Constants.TEST_FOLDER_PATH +
                                   '/' + Constants.FILE_NAME)
        Assertion.assert_cat_file(step=step_5, class_name=TestCase4, steps_quantity=5)
        Assertion.assert_list_of_files(TestCase4)
