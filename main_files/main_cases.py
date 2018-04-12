import sys
import subprocess
import os


class MainCases(object):

    @staticmethod
    def change_folder(path):
        set_path = str(path)
        try:
            os.chdir(set_path)
            return 0
        except BaseException as message:
            return str(message)

    @staticmethod
    def pwd():
        command = subprocess.check_output(['pwd'], shell=True)
        return 'Current working directory is {}'.format(command)

    @staticmethod
    def ls():
        command = subprocess.check_output(['ls'], shell=True)
        return 'List of files is viewed: \n \n {}'.format(command)

    @staticmethod
    def make_directory(folder_name):
        set_folder_name = str(folder_name)
        try:
            subprocess.check_output(['mkdir ./' + set_folder_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def remove_directory(folder_name):
        set_folder_name = str(folder_name)
        try:
            subprocess.check_output(['rmdir ./' + set_folder_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def touch_file(file_name):
        set_file_name = str(file_name)
        try:
            subprocess.check_output(['touch ./' + set_file_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def write_file(file_name, data):
        set_data = str(data)
        try:
            with open(file_name, 'w') as f:
                subprocess.call(['echo', set_data], stdout=f)
            return 0
        except BaseException as Error:
            return str(Error)

    @staticmethod
    def read_file(file_name):
        data = []
        with open(file_name, 'r') as f:
            for line in f:
                data.append(line)
        return data

    @staticmethod
    def cat_file(file_name):
        set_file_path = str(file_name)
        try:
            subprocess.check_output(['cat ' + set_file_path], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def copy_file(file_name, destination_path):
        set_file_name = str(file_name)
        set_destination_path = str(destination_path)
        try:
            subprocess.check_output(['cp ' + set_file_name + " " + set_destination_path], shell=True,
                                    stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def move_file(file_name, destination_path):
        set_file_name = str(file_name)
        set_destination_path = str(destination_path)
        try:
            subprocess.check_output(['mv ' + set_file_name + ' ' + set_destination_path], shell=True,
                                    stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def rename_file(old_file_name, new_file_name):
        return MainCases.move_file(old_file_name, new_file_name)

    @staticmethod
    def remove_file(file_name):
        set_file_name = str(file_name)
        set_removed_asterisks = (set_file_name.replace('*', ''))
        try:
            subprocess.check_output(['rm -f ./' + set_removed_asterisks], shell=True,
                                    stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def execute_script(script_name):
        set_script_name = str(script_name)
        try:
            subprocess.check_output(['sh ' + set_script_name], shell=True, stderr=subprocess.STDOUT)
            return 0
        except subprocess.CalledProcessError as Error:
            return Error.output

    @staticmethod
    def ssh_connect_to_server(host_name, host_ip, command_to_execute):
        set_host_name = str(host_name)
        set_host_ip = str(host_ip)
        command = subprocess.Popen(['ssh -T ' + set_host_name + '@' + set_host_ip + ' '+ command_to_execute],
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            message = command.stderr.readlines()
            sys.stderr.write('{}'.format(message))
        else:
            print(result)
