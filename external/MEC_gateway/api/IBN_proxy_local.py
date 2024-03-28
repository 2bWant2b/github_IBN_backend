import subprocess
import os

this_file_path = os.path.realpath(__file__)
shell_dir = os.path.join(os.path.dirname(os.path.dirname(this_file_path)), "shell_templates")


def get_agent_info():
    # 执行Shell脚本
    shell_path = os.path.normpath(os.path.join(shell_dir, "get_agent_info.sh"))
    os.chmod(shell_path, 0o755)
    result = subprocess.Popen([shell_path], stdout=subprocess.PIPE)
    # 获取脚本输出
    output, error = result.communicate()
    # final_output = ""
    # for i in output:
    #     final_output += i
    #     final_output += "\n"
    return output
    # print(output.decode('utf-8'))


if __name__ == "__main__":
    get_agent_info()
