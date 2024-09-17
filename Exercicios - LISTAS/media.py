x = int(input())
mediaFinal = 0
for i in range(x):
    nota = int(input("Nota: "))
    mediaFinal = mediaFinal + nota
mediaFinal = mediaFinal / x
print(f"A média final é de: {mediaFinal}")    



x = int(input())
y = x
mediaFinal = 0
while x > 0:
    nota = int(input("Nota: "))
    mediaFinal = mediaFinal + nota
    x -= 1
mediaFinal = mediaFinal / y
print(f"A média final é de: {mediaFinal}")    