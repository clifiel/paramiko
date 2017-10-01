import base64

image = open("imagem.gif","rb");
imager = image.read();

#print("Imprimindo a imagem lida")
#print(imager)

image_b64 = base64.b64encode(imager)

#print(image_b64);
