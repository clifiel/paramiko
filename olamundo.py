#!/home/cbernaldo/docs/NetworkAutomation/Projetos/paramiko/bin/python

#Require Python 3.3

import paramiko;

cli = paramiko.client.SSHClient();
cli.set_missing_host_key_policy(paramiko.client.AutoAddPolicy());
cli.connect(hostname="192.168.1.9", username="cbernaldo",password="123456");
#cli.connect(hostname="192.168.1.2", username="cbernaldo");
sdtin, stdout, stderr = cli.exec_command("ls -l ~ | awk '{print $9}'");
stdout.channel.recv_exit_status();

for line in stdout:
	print(line);

#print(type(stdout));
#print(type(sdtin));
#print(type(stderr));

sdtin, stdout, stderr = cli.exec_command("pwd");
stdout.channel.recv_exit_status();
lines = stdout.readlines();
for line in lines:
	print(line);

cli.close();	