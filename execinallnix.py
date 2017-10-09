import paramiko;
from paramiko.ssh_exception import AuthenticationException;

def ConnClient(hostname, username, password):
	#verificar se o paramiko ja foi importado
	ClientSSH = paramiko.client.SSHClient()
	ClientSSH.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())

	try:
		ClientSSH.connect(hostname=hostname, username=username ,password=password)
	except paramiko.ssh_exception.AuthenticationException as e:
		print(e)
		return False
	except paramiko.ssh_exception.NoValidConnectionsError as e:
		print(e)
		return False
	
	return ClientSSH

def CloseClient(ClientSSH):
	#informa se conseguiu fechar a conexao no log
	ClientSSH.close

def ExecCommand(PathToCommands, ClientSSH):
	#verificar se o paramiko ja foi importado
	#verificar se o arquivo do path existe
	#verificar se o objeto do cliente ssh é valido
	with open(PathToCommands,"r") as f:
		CommandList = f.readlines();

		commexecstatus = ""
		#loop para execucao dos comandos de cada linha
		for command in CommandList:
			sdtin, stdout, stderr = ClientSSH.exec_command(command);
			stdout.channel.recv_exit_status();
			#verificar se nao houve erro na execucao do comando; Se sim: manda o erro para o log; Se não: va para o 
			#proximo comando

		#ao acabar os comandos com sucesso retorne true e loge a info
		f.close

	#Valida o status da execucao dos comandos e da o retorno de acordo com a validacao
	return True

hostname="192.168.1.9"
username="cbernaldo"
password="123456"

PathToCommands="commandlist.txt"

if (ConnClient(hostname, username, password)):
	print("Conectado com sucesso.")
	print("Iniciando a execucao de comandos")
	ClientSSH = ConnClient(hostname, username, password)
	ExecCommand(PathToCommands, ClientSSH)
	CloseClient(ClientSSH)
else:
	print("Deu algum problema.")

