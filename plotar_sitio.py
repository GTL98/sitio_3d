## Arquivo com as funções de:
#   - Desenhar os átomos dos aminoácidos pertencentes ao sítio de ligação e;
#   - Os átomos da molécula ligante no sítio de ligação.


def plotar_sitio(lista_coord, tamanho, ver_molecula):
    """
    Função destinada a plotar em um gráfico 3D a conformação do sítio de ligação com a molécula ligante.

    :param lista_coord:
    :param tamanho:
    :param ver_molecula:
    :return gráfico com a disposição do sítio de ligação e a molécula ligante:
    """

    # Importar a biblioteca
    import matplotlib.pyplot as plt

    # Informar as posições das coordenadas XYZ presentes nas tuplas em "lista_coord"
    coord_x = 0
    coord_y = 1
    coord_z = 2

    # Declarar o tipo do gráfico usado
    grafico = plt.figure().add_subplot(projection='3d')

    # Ver somente os aminoácidos
    if not ver_molecula:
        lista_coord.pop(-1)

    # Declarar o espectro de cor para cada grupo de aminoácido
    for i in range(len(lista_coord)):
        aminoacido = lista_coord[i][0]
        # Aminácidos básicos (azul)
        if aminoacido == 'lys':
            cor = 'blue'

        if aminoacido == 'arg':
            cor = 'lightsteelblue'

        if aminoacido == 'his':
            cor = 'royalblue'

        # Aminiácidos ácidos (vermelho)
        if aminoacido == 'asp':
            cor = 'red'

        if aminoacido == 'glu':
            cor = 'lightcoral'

        # Aminoácidos polares(verde)
        if aminoacido == 'asn':
            cor = 'green'

        if aminoacido == 'gln':
            cor = 'lime'

        if aminoacido == 'ser':
            cor = 'greenyellow'

        if aminoacido == 'thr':
            cor = 'mediumseagreen'

        if aminoacido == 'tyr':
            cor = 'springgreen'

        # Aminoácidos apolares (violeta)
        if aminoacido == 'ala':
            cor = 'rebeccapurple'

        if aminoacido == 'val':
            cor = 'blueviolet'

        if aminoacido == 'leu':
            cor = 'mediumorchid'

        if aminoacido == 'ile':
            cor = 'violet'

        if aminoacido == 'pro':
            cor = 'purple'

        if aminoacido == 'phe':
            cor = 'magenta'

        if aminoacido == 'met':
            cor = 'orchid'

        if aminoacido == 'trp':
            cor = 'mediumvioletred'

        if aminoacido == 'gly':
            cor = 'deeppink'

        if aminoacido == 'cys':
            cor = 'hotpink'

        # Molécula ligante (preto)
        if lista_coord[i][0] == 'molecula':
            cor = 'black'

        # Plotar os átomos dos aminoácidos e da molécula lugante no gráfico
        for coord in lista_coord[i][1]:
            x_aa = coord[coord_x]
            y_aa = coord[coord_y]
            z_aa = coord[coord_z]
            grafico.scatter(x_aa, y_aa, z_aa, s=tamanho, color=cor, label=aminoacido.upper())

    # Identificar os eixos do gráfico
    grafico.set_xlabel('Eixo X (Å)')
    grafico.set_ylabel('Eixo Y (Å)')
    grafico.set_zlabel('Eixo Z (Å)')

    # Colocar somente um ponto indicando o aminoácido (ou molécula ligante) na legenda
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))

    # Colocar a legenda na plotagem
    grafico.legend(by_label.values(), by_label.keys(), loc='lower left', bbox_to_anchor=(-0.4, 0.6))

    # Mostrar o gráfico
    plt.show()
