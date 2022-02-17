from plotar_sitio import *
from funcoes_principais import *

nome_arquivo = ''  # path relativo ou path absoluto do arquivo PDB (.pdb)
cadeia_prot = ''   # cadeia da proteína (ex: A ou B ou C ...)
hetatm = ''        # sigla da molécula (ou átomo) a ser analisada (ver no arquivo PDB a sigla da molécula (ou átomo))

def main():
    # Ler o documento
    linhas = ler_documento(nome_arquivo)

    # Obter os aminoácidos de uma determinada cadeia
    cadeia = cadeia_proteina(cadeia_prot, linhas)

    # Obter as coordenadas XYZ da molécula ligante
    molecula = molecula_ligante(hetatm, linhas)

    # Obter os aminoácidos do sítio de ligação e as coordenadas XYZ dos átomos da molécula ligante
    # que estão neste sítio
    sitio, coord_molecula = sitio_ligacao(molecula, cadeia, 4)

    # Obter as coordenadas XYZ dos átomos dos aminoácidos do sítio de ligação
    coord_aminoacidos = atomos_aminoacidos(cadeia_prot, linhas, sitio)

    # Plotar o gráfico
    plotar(coord_aminoacidos, coord_molecula)


if __name__ == '__main__':
    main()
