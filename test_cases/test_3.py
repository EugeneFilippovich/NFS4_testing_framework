from main_files import *


class TestCase3(Commands):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(CustomLogger.console_stdout)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(CustomLogger.file_handler)

    @staticmethod
    def run_test_case():
        TestCase3.logger.info(Constants.INFO_RENAME + Constants.INFO_READ_WRITE_PROPERTY)

        step_1 = Commands.ssh_connect_to_server(host_name=Constants.HOST_USER_NAME, host_ip=Constants.HOST_IP, command_to_execute=Constants.TOUCH_COMMAND +
                                                                                                                                  Constants.HOST_SHARE_PATH + Constants.FILE_NAME)
        Assertion.assert_ssh_to_server(step=step_1, class_name=TestCase3, steps_quantity=1)

        step_2 = Commands.change_folder(Constants.CLIENT_SHARE_PATH)
        Assertion.assert_change_folder(step=step_2, class_name=TestCase3, steps_quantity=2)
        Assertion.assert_working_dir(TestCase3)

        step_3 = Commands.remove_file(Constants.FILE_NAME)
        Assertion.assert_remove_file(step=step_3, class_name=TestCase3, steps_quantity=3)
        Assertion.assert_list_of_files(TestCase3)
