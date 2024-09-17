premio = 780000

g1 = premio * 0.46
g2 = premio * 0.32
g3 = premio - (g1 + g2)

print("O primeiro vencedor receberá a quantia de: R$ ",g1)
print("O segundo vencedor receberá a quantia de: R$ ",g2)
print("O terceiro vencedor receberá a quantia de: R$ ",g3)

ac = premio + (premio * 0.46)

print("O premio acumulado é de: ", ac)