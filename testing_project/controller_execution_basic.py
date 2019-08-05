__author__ = 'Reyaz Ahmad'

import subprocess

class ControllerExec:

    def __init__(self):
        return

    def check_git_version(self):
        """
        git version check
        :return:
        """
        cmd = 'pwd'
        returned_output = subprocess.check_output(cmd)
        print('Output:', returned_output)

    def login(self):
        """
                login without user
                :return:
        """
        cmd = "xprctl login"
        returned_output = subprocess.check_output(cmd)
        print('Output:', returned_output)

    def login_with_user_name(self):
        """
        login with user
        :return:
        """
        cmd = "xprctl login -u user1"
        returned_output = subprocess.check_output(cmd)
        print('Output:', returned_output)

    def logout(self):
        """
        logout
        :return:
        """
        cmd= "xprctl logout"
        returned_output=subprocess.check_output(cmd)
        print('Output:', returned_output)


if __name__=="__main__":
    controller_exec=ControllerExec()
    controller_exec.login()
