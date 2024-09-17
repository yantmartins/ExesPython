mmc = 1

for i in range(2, 21):
    a = mmc
    b = i
    while b != 0:
        a, b = b, a % b
    mdc = a
    mmc = mmc * i // mdc

print(f"O MMC é igual a: {mmc}")
