import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.0.14', username='gillet', password='Admin606')

stdin, stdout, stderr = ssh.exec_command('uptime')

print(stdout.readlines())

ssh.close