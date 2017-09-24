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

