try:
    genero = input("Informe o seu gênero: \n [F] FEMININO; \n [M] MASCULINO; \n [L] LGBT; \n INFORME O SEU: ")
    
    if genero not in ["F", "f", "M", "m", "L", "l"]:
        raise ValueError  # Levanta uma exceção ValueError se a entrada for inválida
    
    if genero == "F" or genero == "f":
        print("Você selecionou FEMININO")
    elif genero == "M" or genero == "m":
        print("Você selecionou MASCULINO")
    elif genero == "L" or genero == "l":
        print("Você selecionou LGBT")
except ValueError:
    print("Você selecionou uma letra inválida")
