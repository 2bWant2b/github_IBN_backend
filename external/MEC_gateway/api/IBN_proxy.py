from external.MEC_gateway.ssh_connection import SSHConnection
import os

this_file_path = os.path.realpath(__file__)
shell_dir = os.path.join(os.path.dirname(os.path.dirname(this_file_path)), "shell_templates")


def get_brief_net_info(device_ip):
    """获取指定设备的简要网络信息"""
    ssh = SSHConnection(device_ip, 22, "lxt", "kc304@KC304")
    ssh.connect()
    # 注意，windows中用反斜杠\，linux中用正斜杠/
    ssh.upload(os.path.normpath(os.path.join(shell_dir, "get_agent_info.sh")))
    return_value = ssh.run_remote_file(get_return_value=True)  # 仅传参
    final_return_value = ""
    for i in return_value:
        final_return_value += i
        final_return_value += "\n"
    ssh.close()
    return final_return_value


def set_ip(device_ip, net_card, ip, con_name="connection1", con_type="ethernet"):
    """设置ip"""
    ssh = SSHConnection(device_ip, 22, "lxt", "kc304@KC304")
    ssh.connect()
    # 注意，windows中用反斜杠\，linux中用正斜杠/
    ssh.upload(os.path.normpath(os.path.join(shell_dir, "set_ip.sh")))
    ssh.run_remote_file(con_name, net_card, con_type, ip)
    ssh.close()


def change_ip(device_ipv4, con_name, ip):
    """修改ip"""
    ssh = SSHConnection(device_ipv4, 22, "lxt", "kc304@KC304")
    ssh.connect()
    # 注意，windows中用反斜杠\，linux中用正斜杠/
    ssh.upload(os.path.normpath(os.path.join(shell_dir, "change_ip.sh")))
    ssh.run_remote_file(con_name, ip)
    ssh.close()


def shutdown_con(device_ip, con_name="connection1"):
    """关闭网卡的连接"""
    ssh = SSHConnection(device_ip, 22, "lxt", "kc304@KC304")
    ssh.connect()
    # 注意，windows中用反斜杠\，linux中用正斜杠/
    ssh.upload(os.path.normpath(os.path.join(shell_dir, "shutdown_connection.sh")))
    return_value = ssh.run_remote_file(con_name)
    ssh.close()


def tcweb_post(device_ip, dev, *args):
    ssh = SSHConnection(device_ip, 22, "lxt", "kc304@KC304")
    ssh.connect()
    ssh.upload(os.path.normpath(os.path.join(shell_dir, "tcweb_post.sh")))
    ssh.run_remote_file(dev, *args)
    ssh.close()


def tcweb_get(device_ip):
    ssh = SSHConnection(device_ip, 22, "lxt", "kc304@KC304")
    ssh.connect()
    ssh.upload(os.path.normpath(os.path.join(shell_dir, "tcweb_get.sh")))
    return_value = ssh.run_remote_file(get_return_value=True)
    print(return_value)


if __name__ == "__main__":
    # get_brief_net_info("192.168.20.199")
    # set_ip("192.168.20.199", "connection1", "enp9s0", "ethernet", r"192.168.168.1/24")
    shutdown_con("192.168.20.156", "connection1")
    # tcweb_post("192.168.20.199", "enp7s0", *["delay", "30ms", "loss", "10%"])
    # tcweb_get("192.168.20.199")
