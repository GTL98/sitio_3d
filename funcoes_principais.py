## Arquivo com as funções de:
#   - Ler o documeto PDB;
#   - Tratar os dados;
#   - Calcular a distância entre os átomos;
#   - Obter os aminoácidos presentes no sítio de ligação;
#   - Obter os átomos desses aminoácidos do sítio de ligação e;
#   - Obter os átomos da molécula ligante.


def ler_documento(nome_documento):
    """
    Função destinada a ler o documento PDB e retornar suas linhas.

    :param nome_documento:
    :return todas as linhas do documento PDB:
    """

    with open(nome_documento, 'r') as doc:
        linhas = doc.readlines()

    return linhas


def cadeia_proteina(cadeia, linhas):
    """
    Função destinada a selecionar os aminoácidos presentes na cadeia informada
    e as coordenadas XYZ de seus átomos.

    :param cadeia:
    :param linhas:
    :return dicionário com o ID do átomo, coordenadas XYZ e o nome do aminoácido:
    """

    atomos = {}

    for linha in linhas:
        linha = linha.strip()

        if linha[0:4] == 'ATOM' and linha[21] == cadeia:
            # ID do átomo (7 - 11)
            id_atomo = int(linha[6:11])

            # ID resíduo aminoácido (23 - 26)
            id_aminoacido = int(linha[22:26])

            # Coordenada X do átomo (31 - 38)
            pos_x = float(linha[30:38])

            # Coordenada Y do átomo (39 - 46)
            pos_y = float(linha[38:46])

            # Coordenada Z do átomo (47 - 54)
            pos_z = float(linha[46:54])

            # Adicionar ao dicionário 'atomos' as informações de posição e qual aminoácido pertencem
            atomos[id_atomo] = (pos_x, pos_y, pos_z, id_aminoacido)

    return atomos


def molecula_ligante(id_molecula, linhas):
    """
    Função destinada a obter as coordenadas XYZ dos átomos da molécula ligante.

    :param id_molecula:
    :param linhas:
    :return dicionário com ID do átomo e as coordenadas XYZ dos átomos da molécula ligante:
    """

    atomos = {}

    for linha in linhas:
        linha = linha.strip()

        if linha[0:6] == 'HETATM' and linha[17:20] == id_molecula:
            # ID do átomo (7 - 11)
            id_atomo = int(linha[6:11])

            # Coordenada X do átomo (31 - 38)
            pos_x = float(linha[30:38])

            # Coordenada Y do átomo (39 - 46)
            pos_y = float(linha[38:46])

            # Coordenada Z do átomo (47 - 54)
            pos_z = float(linha[46:54])

            # Adicionar ao dicionário 'atomos' as coordenadas XYZ de cada átomo da molécula ligante
            atomos[id_atomo] = (pos_x, pos_y, pos_z)

    return atomos


def distancia_euclidiana(x1, y1, z1, x2, y2, z2):
    """
    Função destinada a calcular a distância eucludiana entre os átomos do aminoácido com os átomos
    da molécula ligante.
    A distância eucludiana é calculada como a somatória dos quadrados das diferenças entre as coordenadas.

    :param x1:
    :param y1:
    :param z1:
    :param x2:
    :param y2:
    :param z2:
    :return ditância euclidiana entre os átomos do aminoácido e da molécula ligante:
    """

    # Importar a biblioteca
    import math

    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


def sitio_ligacao(molecula, cadeia, limiar):
    """
    Função destinada a informar quais são os aminoácidos pertencentes ao sítio de ligação
    e as coordenadas XYZ dos átomos da molécula ligante que estão neste sítio.

    :param molecula:
    :param cadeia:
    :param limiar:
    :return uma lista com os aminoácidos que fazem parte do sítio de ligação
    e uma lista com as coordenadas XYZ da molécula ligante que está no sítio de ligação:
    """

    # Informar as posições das informações nos dicionários usados
    x = 0
    y = 1
    z = 2
    info = 3

    # Criar as listas que armazenarão os IDs dos aminoácidos do sítio de ligação
    # e as coordenadas XYZ dos átomos da molécula ligante
    sitio = []
    coord_molecula = []

    # Verificar se a distância entre os átomos dos aminoácidos e da molécula ligante
    # estão distantes até um certo valor declarado por 'limiar'
    for m in molecula:
        for c in cadeia:
            d = distancia_euclidiana(molecula[m][x], molecula[m][y], molecula[m][z],
                                     cadeia[c][x], cadeia[c][y], cadeia[c][z])
            if d <= limiar:
                # Isso evita que tenha informações repetidas nas listas
                if not cadeia[c][info] in sitio:
                    sitio.append(cadeia[c][info])
                if not (molecula[m][x], molecula[m][y], molecula[m][z]) in coord_molecula:
                    coord_molecula.append((molecula[m][x], molecula[m][y], molecula[m][z]))

    return sitio, coord_molecula


def atomos_aminoacidos(cadeia, linhas, sitio):
    """
    Função destinada a obter as coordenadas XYZ dos átomos dos aminoácidos pertencentes ao sítio de ligação.

    :param cadeia:
    :param linhas:
    :param sitio:
    :return uma lista com as coordenadas XYZ dos átomos pertencentes ao sítio de ligação:
    """

    atomos = []

    for linha in linhas:
        linha = linha.strip()

        if linha[0:4] == 'ATOM' and linha[21] == cadeia:
            # ID do aminoácido (23 - 26)
            id_aminoacido = int(linha[22:26])

            # Coordenada X do átomo (31 - 38)
            pos_x = float(linha[30:38])

            # Coordenada Y do átomo (39 - 46)
            pos_y = float(linha[38:46])

            # Coordenada Z do átomo (47 - 54)
            pos_z = float(linha[46:54])

            # Verificar se o aminoácido analisado está no sítio de ligação
            if id_aminoacido in sitio:
                atomos.append((pos_x, pos_y, pos_z))

    return atomos

