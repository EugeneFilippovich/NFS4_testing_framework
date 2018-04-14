from main_files import *


if __name__ == '__main__':

    # SetUp condition with read-write permissions
    set_up.SetUp.insert_file(Constants.SERVER_IP, Constants.SERVER_NAME, Constants.DIRECTORY_PATH_STATEMENTS,
                             Constants.FILE_PATH_STATEMENT, Constants.READ_WRITE_ACCESS)
    set_up.SetUp.ssh_export_to_host(Constants.SERVER_NAME, Constants.SERVER_IP, Constants.RESTART_NFS)

    test_1.TestCase1.run_test_case()
    clean_up.Cleaner.clean_up_folder()

    test_2.TestCase2.run_test_case()
    clean_up.Cleaner.clean_up_folder()

    test_3.TestCase3.run_test_case()
    clean_up.Cleaner.clean_up_folder()

    test_4.TestCase4.run_test_case()
    clean_up.Cleaner.clean_up_folder()
    clean_up.Cleaner.delete_test_folder()

    test_5.TestCase5.run_test_case()
    clean_up.Cleaner.clean_up_folder()
    clean_up.Cleaner.delete_test_folder()

    test_6.TestCase6.run_test_case()
    clean_up.Cleaner.clean_up_folder()

    # SetUp condition with read-only permissions
    set_up.SetUp.insert_file(Constants.SERVER_IP, Constants.SERVER_NAME, Constants.DIRECTORY_PATH_STATEMENTS,
                             Constants.FILE_PATH_STATEMENT, Constants.READ_ONLY_ACCESS)
    set_up.SetUp.ssh_export_to_host(Constants.SERVER_NAME, Constants.SERVER_IP, Constants.RESTART_NFS)

    test_7.TestCase7.run_test_case()
    clean_up.Cleaner.clean_up_folder()

    test_8.TestCase8.run_test_case()
    clean_up.Cleaner.clean_up_folder()

    test_9.TestCase9.run_test_case()
    clean_up.Cleaner.clean_up_folder()

    test_10.TestCase10.run_test_case()
    clean_up.Cleaner.clean_up_folder()