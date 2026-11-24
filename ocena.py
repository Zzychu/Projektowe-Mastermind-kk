# tabela = [ 1, 2, 3, 4]
# uzyt = [ 0, 1, 3, 4]

def ocena(tabela, uzyt):
    tabela_ocen = []
    for i in range(len(uzyt)):
        if uzyt[i] == tabela[i]:
            tabela_ocen.append("!")
        elif uzyt[i] in tabela:
            tabela_ocen.append(".")
        else:
            tabela_ocen.append("#")
    return tabela_ocen