'''
#lendo o arquivo inteiro
file = open("../b64.txt","r");
print(file.read());

#lendo os tres primeiros caracteres
file = open("../b64.txt","r");
print(file.read(3));

#lendo apenas uma linha inteira
file = open("../b64.txt","r");
print(file.readline());

#lendo todas as linhas (linha a linha)
file = open("../b64.txt","r");
print(file.readlines());
'''

#fazendo uso do statement with
with open("arquivo.txt","r") as file:
	arquivo = file.readlines();

	print("Imprimindo informações do arquivo: " + file.name)
	print(arquivo);

	print("Imprimindo linha especifica do arquivo: " + file.name)
	print(arquivo[1]);

	file.close

#apresentando o texto lido para o usuario
with open("arquivo.txt","r") as f:
	print("\nImprimindo o arquivo inteiro para o usuario\n")
	for linha in f.readlines():
		print(linha);

#usando split em uma linha
with open("arquivo.txt","r") as f:	
	data = f.readlines();

	print("\nImprimindo as palavras splitadas\n");

	for linha in data:
		palavras = linha.split();
		for palavra in palavras:		
			if palavra == 'Quarta':
				print("cheguei na quarta linha");				
		print(palavras);

