from main_files import *


class TestCase9(Commands):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase9.logger.info(Constants.INFO_RENAME + Constants.INFO_READ_ONLY_PROPERTY)

        step_1 = Commands.ssh_connect_to_server(host_name=Constants.HOST_USER_NAME, host_ip=Constants.HOST_IP,
                                                command_to_execute=Constants.TOUCH_COMMAND + Constants.HOST_SHARE_PATH +
                                                Constants.FILE_NAME)
        Assertion.assert_ssh_to_server(step=step_1, class_name=TestCase9, steps_quantity=1)

        step_2 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step=step_2, class_name=TestCase9, steps_quantity=2)
        Assertion.assert_working_dir(TestCase9)

        step_3 = Commands.rename_file(Constants.FILE_NAME, Constants.FILE_NAME2)
        Assertion.assert_rename_file(step=step_3, class_name=TestCase9, steps_quantity=3)
        Assertion.assert_list_of_files(TestCase9)
