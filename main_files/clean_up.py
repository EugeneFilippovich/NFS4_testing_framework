import subprocess
import sys
from main_files.constants import Constants


class Cleaner(object):
    @staticmethod
    def clean_up_folder():
        command = subprocess.Popen(["ssh -T " + Constants.SERVER_NAME + '@' + Constants.SERVER_IP + ' ' +
                                    Constants.CLEAN_SERVER_FOLDER], shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            message = command.stderr.readlines()
            sys.stderr.write("{}".format(message))
        else:
            print(result)

    @staticmethod
    def delete_test_folder():
        subprocess.call([Constants.CLEAN_TEST_FOLDER], shell=True)
