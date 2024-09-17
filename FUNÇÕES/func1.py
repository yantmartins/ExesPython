def verifica_idade(idade):
    if idade >= 18:
        return "MAIOR DE IDADE"
    else:
        return "MENOR DE IDADE"
    
i = int(input("Digite a idade: "))

resultado = verifica_idade(i)

print(resultado)    
