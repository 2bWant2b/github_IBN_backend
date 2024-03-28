import paramiko
import os


class SSHConnection:
    """
    用于建立本机与意图驱动代理的连接，传输sh文件，执行与反馈
    ssh = SSHConnection("192.168.20.199",22,"lxt","kc304@KC304")
    ssh.connect()
    # 注意，windows中用反斜杠\，linux中用正斜杠/
    ssh.upload(r"D:\ourproject\Intent_driven_network\IBN_v1\back_end_project\external\MEC_gateway\shell_templates\set_ip.sh")
    ssh.run_remote_file("enp9s0")
    ssh.close()
    """

    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.__transport = None
        self.target_file_path = None

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    def upload(self, original_file_path, target_file_name="sh_script.sh"):
        target_file_path = "/tmp/{}".format(target_file_name)
        self.target_file_path = target_file_path
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        try:
            sftp.put(original_file_path, target_file_path)
        except FileNotFoundError as e:
            print(e)
            print("can not find \"{}\"".format(original_file_path))
        else:
            print("file transfer successful")

    def run_remote_file(self, *args, ssh_file_path=None, get_return_value=False):
        """仅传参即可，所有参数需要是字符串形式，并且与sh文件中的参数顺序一致，如果想指定linux上的文件，需要以关键词的形式传参"""
        ssh_file_path = ssh_file_path or self.target_file_path  # NB
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
        ssh._transport = self.__transport
        dos2unix_val = "dos2unix " + ssh_file_path + ";"
        chmod = "sudo chmod 755 {};".format(ssh_file_path)  # 修改权限
        str_args = " ".join(args)
        remote_cmd = dos2unix_val + chmod + "sudo " + ssh_file_path + " " + str_args
        stdin, stdout, stderr = ssh.exec_command(remote_cmd, get_pty=True)
        stdin.write(self.password + "\n")  # 输入密码
        result = stdout.read().decode()
        result_list = result.split("\n")
        for i in range(len(result_list)):
            if i >= 2:
                print(result_list[i])
        if get_return_value:
            return result_list[3:]


if __name__ == "__main__":
    ssh = SSHConnection("192.168.20.199", 22, "lxt", "kc304@KC304")
    ssh.connect()
    # 注意，windows中用反斜杠\，linux中用正斜杠/
    ssh.upload(
        r"D:\ourproject\Intent_driven_network\IBN_v1\back_end_project\external\MEC_gateway\shell_templates\set_ip.sh")

    ssh.run_remote_file()  # 仅传参
    ssh.close()
