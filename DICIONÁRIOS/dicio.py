### Exemplo de DICIONÁRIO com CHAVES e VALORES
empresa = {
    'razaosocial':'Zaine',
    'cidade':'Ilhabela',
    'estado': 'SP',
    'ganhos':15.99
}

###Percorrer um DICIONÁRIO com FOR dicio.keys() imprime as CHAVES e dicio.values() imprime os VALORES
for item in empresa.keys():
    print(item)

print()

for item in empresa.values():
    print(item)

print()

## KEY e VALUE em forma simplificada e organizada
for k,v in empresa.items():
    print(f"{k} : {v}")    