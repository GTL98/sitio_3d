## Arquivo com as funções de:
#   - Ler o documeto PDB;
#   - Tratar os dados;
#   - Calcular a distância entre os átomos;
#   - Obter os aminoácidos presentes no sítio de ligação;
#   - Obter os átomos desses aminoácidos do sítio de ligação;
#   - Obter os átomos da molécula ligante e;
#   - Plotar os átomos.


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

    atomos_cadeia = {}

    for linha in linhas:
        if linha[0:4] == 'ATOM' and linha[21] == cadeia:
            # ID do átomo (7 - 11)
            id_atomo = int(linha[6:11])

            # ID resíduo aminoácido (23 - 26)
            id_residuo = int(linha[22:26])

            # Nome do aminoácido (18 - 20)
            nome_aa = str(linha[17:20]).lower().strip()

            # Coordenada X do átomo (31 - 38)
            x = float(linha[30:38])

            # Coordenada Y do átomo (39 - 46)
            y = float(linha[38:46])

            # Coordenada Z do átomo (47 - 54)
            z = float(linha[46:54])

            # Adicionar ao dicionário 'atomos_cadeia' as informações de posição e qual aminoácido pertencem
            atomos_cadeia[id_atomo] = (x, y, z, id_residuo, nome_aa)

    return atomos_cadeia


def molecula_ligante(id_molecula, linhas):
    """
    Função destinada a obter as coordenadas XYZ dos átomos da molécula ligante.

    :param id_molecula:
    :param linhas:
    :return dicionário com ID do átomo e as coordenadas XYZ dos átomos da molécula ligante:
    """

    atomos_molecula = {}

    for linha in linhas:
        if linha[0:6] == 'HETATM' and linha[17:20] == id_molecula:
            # ID do átomo (7 - 11)
            id_atomo = int(linha[6:11])

            # Coordenada X do átomo (31 - 38)
            x = float(linha[30:38])

            # Coordenada Y do átomo (39 - 46)
            y = float(linha[38:46])

            # Coordenada Z do átomo (47 - 54)
            z = float(linha[46:54])

            # Adicionar ao dicionário 'atomos_molecula' as coordenadas XYZ de cada átomo da molécula ligante
            atomos_molecula[id_atomo] = (x, y, z)

    return atomos_molecula


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

    # Informar as posições das coordenadas XYZ presentes nas tuplas em "cadeia" e "molecula"
    x = 0
    y = 1
    z = 2
    id_residuo = 3

    # Criar as listas que armazenarão os IDs dos aminoácidos do sítio de ligação
    # e as coordenadas XYZ dos átomos da molécula ligante
    sitio = []
    coord_molecula = []

    # Verificar se a distância entre os átomos dos aminoácidos e da molécula ligante
    # estão distantes até um certo valor declarado por "limiar"
    for m in molecula:
        for c in cadeia:
            d = distancia_euclidiana(molecula[m][x], molecula[m][y], molecula[m][z],
                                     cadeia[c][x], cadeia[c][y], cadeia[c][z])
            if d <= limiar:
                # Isso evita que tenha informações repetidas nas listas
                if not cadeia[c][id_residuo] in sitio:
                    sitio.append(cadeia[c][id_residuo])
                if not (molecula[m][x], molecula[m][y], molecula[m][z]) in coord_molecula:
                    coord_molecula.append((molecula[m][x], molecula[m][y], molecula[m][z]))

    return sitio, coord_molecula


def atomos_aminoacidos_sitio(cadeia_info, sitio):
    """
    Função destinada a obter as coordenadas XYZ dos átomos dos aminoácidos pertencentes ao sítio de ligação.

    :param cadeia_info:
    :param sitio:
    :return uma lista com as coordenadas XYZ dos átomos pertencentes ao sítio de ligação:
    """

    atomos = []
    for s in sitio:
        for chave, valor in cadeia_info.items():
            if s == valor[-2]:
                # Chave: nome abreviado do aminoácido
                # Valor: tupla com as coordenadas XYZ de cada átomo do aminoácido
                atomos.append({valor[-1]: (valor[0], valor[1], valor[2])})

    return atomos


def juntar_atomos_aminoacidos_sitio(lista_aa):
    """
    Função destinada a colocar todas as posições XYZ do mesmo aminoácido em uma única chave.

    :param lista_aa:
    :return dicionário com as chaves sendo os aminoácidos do sítio de ligação e os valores as posições
    XYZ de cada átomo deste aminoácido:
    """

    # Colocar cada aminoácido presente no sítio de liação somente UMA vez na lista
    lista = []
    for x in lista_aa:
        for y in x.keys():
            if not y in lista:
                lista.append(y)

    # Criar um dicionário a partir dos aminoácidos presentes em "lista"
    dic = dict.fromkeys(lista)
    for chave, valor in dic.items():
        if valor is None:
            dic[chave] = []

    # Adicionar à cada chave as posições XYZ dos átomos dos aminoácidos do sítio de ligação
    for k in lista:
        for z in lista_aa:
            for c, v in z.items():
                if c == k:
                    dic[c].append(v)

    return dic


def plotar_aminoacidos(coord_aa, coord_molecula, tamanho, ver_molecula):
    """
    Função destinada a mostrar tridimensionalmente o sítio de ligação da proteína.

    :param coord_aa:
    :param coord_molecula:
    :param tamanho:
    :param ver_molecula:
    :return:
    """

    # Importar o arquivo da plotagem do gráfico
    import plotar_sitio

    # Criar uma lista com todos os aminoácidos
    lista_aa = ['ala', 'arg', 'asn', 'asp', 'cys',
                'gln', 'glu', 'gly', 'his', 'ile',
                'leu', 'lys', 'met', 'phe', 'pro',
                'ser', 'thr', 'try', 'trp', 'val']

    # Criar uma lista com tuplas que contêm o aminoácido e as coordenadas de seus átomos
    lista_final = []

    for chave, valor in coord_aa.items():
        # Se o aminoácido estiver no sítio, então adicione-o à "lista_final"
        if chave in lista_aa:
           lista_final.append((chave, valor))

    # Adicionar a molécula ligante à "lista_final" na última posição
    lista_final.append(('molecula', coord_molecula))

    # Chamar a função da plotagem do gráfico
    plotar_sitio.plotar_sitio(lista_final, tamanho, ver_molecula)
