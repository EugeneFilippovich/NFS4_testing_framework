import sys
import paramiko
import subprocess


class SetUp(object):

    @staticmethod
    def insert_file(host, user, directory, filename, data):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user)
        sftp = ssh.open_sftp()
        try:
            sftp.mkdir(directory)
        except IOError:
            pass
        f = sftp.open(directory + "/" + filename, "w")
        f.write(data)
        f.close()
        ssh.close()

    @staticmethod
    def ssh_export_to_host(host_name, host_ip, client_command):
        set_host_name = str(host_name)
        set_host_ip = str(host_ip)
        command = subprocess.Popen(["ssh -T " + set_host_name + '@' + set_host_ip + ' ' + client_command],
                                   shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = command.stdout.readlines()
        if result == 0:
            message = command.stderr.readlines()
            sys.stderr.write("{}".format(message))
        else:
            print(result)

