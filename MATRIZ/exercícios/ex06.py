X = [[40,30,20],
     [17,16,14],
     [19,15,18]]
Y = [[31,32,33],
     [21,22,23],
     [12,13,19]]

Z = []

i = 0
while i < len(X):
    linhaZ = []
    j = 0
    while j < len(X[i]):
        soma = X[i][j] + Y[i][j]
        linhaZ.append(soma)
        j += 1
    Z.append(linhaZ)
    i +=1    

i= 0
while i < len(X):
    print(X[i])
    i += 1

print()
i= 0
while i < len(Y):
    print(Y[i])
    i += 1

print()
i= 0
while i < len(Z):
    print(Z[i])
    i += 1    