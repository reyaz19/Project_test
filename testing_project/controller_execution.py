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

    def modify_user(self):
        """
        To modify user
        :return:
        """
        cmd= " xprctl register_cluster -f /home/xpresso/register.json"
        returned_output=subprocess.check_output(cmd)
        print('Output:', returned_output)

    def build_project(self):
        """
        To build project
        :return:
        """
        cmd= "xprctl build_project -f /home/xpresso/build.json"
        returned_output=subprocess.check_output(cmd)
        print('Output:', returned_output)

    def deploy_project(self):
        """
        To deploy project
        :return:
        """
        cmd= "xprctl deploy_project -f /home/xpresso/deploy.json"
        returned_output=subprocess.check_output(cmd)
        print('Output:', returned_output)

    def undeploy_project(self):
        """
        To undeploy project
        :return:
        """
        cmd= "xprctl undeploy_project -f /home/xpresso/undeploy.json"
        returned_output=subprocess.check_output(cmd)
        print('Output:', returned_output)


    def create_project(self):
        """
        To create project
        :return:
        """
        cmd= "xprctl create_project -f /home/xpresso/create_project.json"
        returned_output=subprocess.check_output(cmd)
        print('Output:', returned_output)


control = ControllerExec()
control.check_git_version()
'''
control.login()
control.login_with_user_name()
control.logout()
control.modify_user()
control.build_project()
control.deploy_project()
control.undeploy_project()
control.create_project()
'''



