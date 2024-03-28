import subprocess


def get_agent_info():
    # 执行Shell脚本
    result = subprocess.Popen(['../shell_templates/get_agent_info.sh'], stdout=subprocess.PIPE)
    # 获取脚本输出
    output, error = result.communicate()
    print(output.decode('utf-8'))
