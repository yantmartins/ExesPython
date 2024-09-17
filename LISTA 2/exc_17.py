altura = float(input("Digite a sua altura:"))
sexo = input("Informe M para MASCULINO ou F para FEMININO: ")


if sexo == "M":
    print("O peso ideal é: ", altura * 72.7 - 58)
else:
    print("O peso ideal é: ", altura * 62.1 - 44.7)    
    