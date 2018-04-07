import sys
import subprocess
# TODO
import constants as cons


class Cleaner(object):
    @staticmethod
    def clean_up_folder():
        command = subprocess.Popen(["ssh -T " + cons.Constants.SERVER_NAME + '@' + cons.Constants.SERVER_IP + ' ' +
                                    cons.Constants.CLEAN_SERVER_FOLDER], shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            message = command.stderr.readlines()
            sys.stderr.write("{}".format(message))
        else:
            print(result)

    @staticmethod
    def delete_test_folder():
        subprocess.call([cons.Constants.CLEAN_TEST_FOLDER], shell=True)
