import paramiko;

def ConnClient(hostname, username, password):
	#verificar se o paramiko ja foi importado
	ClientSSH = paramiko.client.SSHClient()
	ClientSSH.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
	ClientSSH.connect(hostname=hostname, username=username ,password=password)
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

