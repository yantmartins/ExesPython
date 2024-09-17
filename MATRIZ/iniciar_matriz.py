#### MATRIZ 4X4 COM ZEROS
l = 4
c = 4
matriz = [] ##COMEÇA VAZIA E VAI SER PREENCHIDA COM A "linha []"
i = 0
### INICIALIZAR E PREENCHER A MATRIZ
while i <l: ## PRIMEIRO O WHILE PREENCHE AS LINHAS DA MATRIZ DEFINIDAS NA VAR "l"
    linha = [] ## criar a linha que vai preencher na matriz
    j = 0 ## contador do while para preencher as colunas
    while j < c:
        linha.append(0) ## preenche a coluna com 0
        j += 1
    matriz.append(linha) ## adiciona na matriz a lista gerada 
    i += 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1
