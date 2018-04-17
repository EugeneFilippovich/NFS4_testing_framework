from main_files import *


if __name__ == '__main__':

    # SetUp condition with read-write permissions
    SetUp.insert_file(host_name=Constants.HOST_IP, user_name=Constants.HOST_USER_NAME, directory=Constants.DIRECTORY_PATH_STATEMENTS,
                      filename=Constants.FILE_PATH_STATEMENT, data=Constants.READ_WRITE_ACCESS)
    SetUp.ssh_export_to_host(host_name=Constants.HOST_USER_NAME, host_ip=Constants.HOST_IP, client_command=Constants.RESTART_NFS)

    TestCase1.run_test_case()
    Cleaner.clean_up_folder()

    TestCase2.run_test_case()
    Cleaner.clean_up_folder()

    TestCase3.run_test_case()
    Cleaner.clean_up_folder()

    TestCase4.run_test_case()
    Cleaner.clean_up_folder()
    Cleaner.delete_test_folder()

    TestCase5.run_test_case()
    Cleaner.clean_up_folder()
    Cleaner.delete_test_folder()

    TestCase6.run_test_case()
    Cleaner.clean_up_folder()

    # SetUp condition with read-only permissions
    SetUp.insert_file(host_name=Constants.HOST_IP, user_name=Constants.HOST_USER_NAME, directory=Constants.DIRECTORY_PATH_STATEMENTS,
                      filename=Constants.FILE_PATH_STATEMENT, data=Constants.READ_ONLY_ACCESS)
    SetUp.ssh_export_to_host(host_name=Constants.HOST_USER_NAME, host_ip=Constants.HOST_IP, client_command=Constants.RESTART_NFS)

    TestCase7.run_test_case()
    Cleaner.clean_up_folder()

    TestCase8.run_test_case()
    Cleaner.clean_up_folder()

    TestCase9.run_test_case()
    Cleaner.clean_up_folder()

    TestCase10.run_test_case()
    Cleaner.clean_up_folder()
