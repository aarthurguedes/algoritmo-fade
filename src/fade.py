#coding: utf-8

# Universidade Federal de Campina Grande - UFCG
# Arthur Silva Lima Guedes - 118110410
# Atividade 3 - FMCC2
# Professor: Thiago Emmanuel

from PIL import Image

# Função principal
def main():
	
	# Carregando as imagens
	imagem1 = Image.open("../input/img1.jpg")
	imagem2 = Image.open("../input/img2.jpg")

	# Usando a função get_vetor para cada uma das imagens
	vetor_imagem1 = get_vetor(imagem1)
	vetor_imagem2 = get_vetor(imagem2)

	for i in range(11):
		vetor = get_vetor_final(vetor_imagem1, vetor_imagem2, 1 - (i * 0.1), (i * 0.1))
		nova_imagem = transformar_vetor_em_imagem(vetor, imagem1.size[0], imagem2.size[1])
		nova_imagem.show()
		nova_imagem.save("../output/fade" + str(i) + ".JPG")

# Criando uma função que recebe como parâmetro uma imagem e retorna o vetor que a representa
def get_vetor(imagem):
	vetor = []
	largura, altura = imagem.size
	
	for y in range(altura):
		for x in range(largura):
			vetor.append(imagem.getpixel((x,y)))
	
	return vetor

# Função que recebe como parâmetro dois vetores (representando duas imagens) e dois escalares 
# Com isso, calcula o produto por escalar e retorna o vetor resultante da soma dos vetores após a multiplicação
def get_vetor_final(vetor1, vetor2, escalar1, escalar2):
	vetor_final = []
	
	for i in range(len(vetor1)):
		produto_por_escalar1 = (int(vetor1[i][0] * escalar1), int(vetor1[i][1] * escalar1), int(vetor1[i][2] * escalar1))
		produto_por_escalar2 = (int(vetor2[i][0] * escalar2), int(vetor2[i][1] * escalar2), int(vetor2[i][2] * escalar2))
		
		vetor_final.append((produto_por_escalar1[0] + produto_por_escalar2[0], produto_por_escalar1[1] + produto_por_escalar2[1], produto_por_escalar1[2] + produto_por_escalar2[2]))
	
	return vetor_final

# Função que faz o processo inverso das anteriores: 
# a partir do vetor, largura e altura que recebe como parâmetros, gera e retorna a imagem que representa esse vetor
def transformar_vetor_em_imagem(vetor, largura, altura):
	imagem = Image.new("RGB", (largura, altura))
	pixels = imagem.load()
	
	i = 0
	for y in range(altura):
		for x in range(largura):
			pixels[x,y] = vetor[i]
			i += 1
	
	return imagem

# Chamada da função principal
if __name__ == "__main__":
	main()
