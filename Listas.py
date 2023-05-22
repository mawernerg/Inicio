def prnt(lenin):
    for i in lenin:
        print(lenin[i - 1])
    return


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prnt(lista)

lista.pop()

lista.reverse()
algo = lista

print(algo)
prnt(algo)