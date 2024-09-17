notas = []
while True:
 nota = float(input("Informe uma nota; ou um valor negativo para encerrar:  "))
 if 0 <= nota <= 10:
  notas.append(nota)
 else:
  break

if len(notas) > 0:
 media = sum(notas) / len(notas)
 print(f"A media das notas é {media}")
else:
 print("Nenhuma nota válida foi informada")