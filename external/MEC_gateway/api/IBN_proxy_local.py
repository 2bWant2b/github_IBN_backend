import subprocess
import os

this_file_path = os.path.realpath(__file__)
shell_dir = os.path.join(os.path.dirname(os.path.dirname(this_file_path)), "shell_templates")


def get_agent_info(method):
    shell_path = os.path.normpath(os.path.join(shell_dir, "get_agent_info.sh"))
    os.chmod(shell_path, 0o755)
    result = subprocess.Popen([shell_path, method], stdout=subprocess.PIPE)
    output, error = result.communicate()
    return output.decode('utf-8')


def change_agent_ip(net_card, ip):
    shell_path = os.path.normpath(os.path.join(shell_dir, "change_agent_ip.sh"))
    os.chmod(shell_path, 0o755)
    result = subprocess.Popen([shell_path, net_card, ip], stdout=subprocess.PIPE)
    output, error = result.communicate()

