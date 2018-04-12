

class Constants(object):
    SERVER_NAME = 'root'
    # TODO
    SERVER_IP = '192.168.1.103'

    TOUCH_COMMAND = 'touch '
    READ_ONLY_ACCESS = '/share *(ro,sync)'
    READ_WRITE_ACCESS = '/share *(rw,sync)'
    RESTART_NFS = 'exportfs -arv'
    DIRECTORY_PATH_STATEMENTS = '/etc'
    FILE_PATH_STATEMENT = '/exports'

    CLEAN_SERVER_FOLDER = 'rm -f /share/*'
    # TODO
    CLEAN_TEST_FOLDER = 'rm -rf /home'

    FILE_NAME = 'test'
    FILE_NAME2 = 'test_2'
    DIRECTORY_NAME = 'TEST_FOLDER'
    TEST_STRING = 'echo "File has been written. Success!"'

    INFO_READ_ONLY_PROPERTY = 'Condition *(ro, sync)'
    INFO_READ_WRITE_PROPERTY = 'Condition *(rw, sync)'
    INFO_CREATE = 'Create a file in the share directory. '
    INFO_RENAME = 'Rename a file from the share directory. '
    INFO_REMOVE = 'Remove a file from the share directory. '
    INFO_COPY = 'Copy a file to the share directory. '
    INFO_MOVE = 'Move a file into the share directory. '
    INFO_EXECUTE = 'Execute a file from the share directory. '
    INFO_WRITE_DATA = 'Write data into a file from the share directory. '

    CLIENT_SHARE_PATH = '/mnt/share'
    HOST_SHARE_PATH = '/share'
    # TODO
    LOGGER_PATH = '/home/masya/Masyalee/PyCharm_projects/NFSv4_share/'
    TEST_FOLDER_PATH = '/home/masya/Masyalee/PyCharm_projects/NFSv4_share/'