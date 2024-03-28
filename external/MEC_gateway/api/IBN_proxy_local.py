import subprocess
import os


def get_agent_info():
    # 执行Shell脚本
    shell_path = '../shell_templates/get_agent_info.sh'
    os.chmod(shell_path, 0o755)
    result = subprocess.Popen([shell_path], stdout=subprocess.PIPE)
    # 获取脚本输出
    output, error = result.communicate()
    print(output.decode('utf-8'))


if __name__ == "__main__":
    get_agent_info()
