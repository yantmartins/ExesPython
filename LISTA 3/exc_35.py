vetor = ["y", "a", "n", "t", "o", "r", "r", "e", "s", "m"]
consoantes = []

for letra in vetor:
    if letra not in ["a", "e", "i", "o", "u"]:
        consoantes.append(letra)

print(f"Foram lidas {len(consoantes)} consoantes que são: {consoantes}")
