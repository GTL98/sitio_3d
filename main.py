# Importar o arquivo com as funções principais
from funcoes_principais import *

# Path relativo ou absoluto do arquivo PDB (.pdb)
nome_arquivo = ''

# Cadeia da proteína (ex: A ou B ou C ...)
cadeia_prot = ''

# Sigla da molécula ligante (ou átomo)
hetatm = ''

# Determinar o limiar de distância entre os átomos dos aminoácidos do sítio de ligação
# e os átomos da molécula ligante
limiar = 0

# Determinar o tamanho dos pontos que serão plotatos no gráfico (padrão 50)
tamanho = 50

# Se "True" é possível ver a molécula na plotagem. Se "False" não é possível de ver a
# molécula na plotagem (padrão "True")
ver_molecula = True


def main():
    # Ler o documento
    linhas = ler_documento(nome_arquivo)

    # Obter os aminoácidos de uma determinada cadeia
    cadeia = cadeia_proteina(cadeia_prot, linhas)

    # Obter as coordenadas XYZ da molécula ligante
    molecula = molecula_ligante(hetatm, linhas)

    # Obter os aminoácidos do sítio de ligação e as coordenadas XYZ dos átomos da molécula ligante
    # que estão neste sítio
    sitio, coord_molecula = sitio_ligacao(molecula, cadeia, limiar)

    # Obter as coordenadas XYZ dos átomos dos aminoácidos do sítio de ligação
    atomos_aa_sitio = atomos_aminoacidos_sitio(cadeia, sitio)

    # Juntar as coordenadas dos átomos dos aminoácidos em um dicionário para que haja somente um
    # aminoácido como chave e o valor seja todas as coordenadas desse aminoácido, ou seja, se houver
    # mais de um mesmo aminoácido, colocar essas coordenadas na mesma chave
    coord_aminoacidos = juntar_atomos_aminoacidos_sitio(atomos_aa_sitio)

    # Plotar o gráfico
    plotar_aminoacidos(coord_aminoacidos, coord_molecula, tamanho, ver_molecula)


if __name__ == '__main__':
    main()
