import subprocess

def login():
    """
    login without user
    :return:
    """
    cmd="xprctl login"

    returned_output = subprocess.check_output(cmd)
    print('Output:', returned_output)


def login_with_user_name():
    """
    login with user
    :return:
    """
    cmd = "xprctl login -u user1"
    returned_output = subprocess.check_output(cmd)
    print('Output:', returned_output)


def logout():
    """
    logout
    :return:
    """
    cmd= "xprctl logout"
    returned_output=subprocess.check_output(cmd)
    print('Output:', returned_output)


def modify_user():
    """
    To modify user
    :return:
    """
    cmd= " xprctl register_cluster -f /home/xpresso/register.json"
    returned_output=subprocess.check_output(cmd)
    print('Output:', returned_output)


def build_project():
    """
    To build project
    :return:
    """
    cmd= "xprctl build_project -f /home/xpresso/build.json"
    returned_output=subprocess.check_output(cmd)
    print('Output:', returned_output)


def deploy_project():
    """
    To deploy project
    :return:
    """
    cmd= "xprctl deploy_project -f /home/xpresso/deploy.json"
    returned_output=subprocess.check_output(cmd)
    print('Output:', returned_output)


def undeploy_project():
    """
    To undeploy project
    :return:
    """
    cmd= "xprctl undeploy_project -f /home/xpresso/undeploy.json"
    returned_output=subprocess.check_output(cmd)
    print('Output:', returned_output)


def create_project():
    """
    To create project
    :return:
    """
    cmd= "xprctl create_project -f /home/xpresso/create_project.json"
    returned_output=subprocess.check_output(cmd)
    print('Output:', returned_output)



