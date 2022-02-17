## Arquivo com as funções de:
#   - Desenhar os átomos dos aminoácidos pertencentes ao sítio de ligação e;
#   - Os átomos da molécula ligante no sítio de ligação.


def plotar(atomos_aminoacidos, atomos_molecula,
           t_aa=50, cor_aa='red', ver_aa=True,
           t_ml=50, cor_ml='green', ver_ml=True):
    """
    Função destinada a plotar em um gráfico 3D a conformação do sítio de ligação com a molécula ligante.

    :param atomos_aminoacidos:
    :param atomos_molecula:
    :return gráfico com a disposição do sítio de ligação e a molécula ligante:
    """

    # Importar a biblioteca
    import matplotlib.pyplot as plt

    # Informar as posições das informações nas listas usados
    coord_x = 0
    coord_y = 1
    coord_z = 2

    # Declarar o tipo do gráfico usado
    grafico = plt.figure().add_subplot(projection='3d')

    # Plotar os átomos dos aminoácidos no gráfico
    if ver_aa:
        for atomo_aa in atomos_aminoacidos:
            x_aa = atomo_aa[coord_x]
            y_aa = atomo_aa[coord_y]
            z_aa = atomo_aa[coord_z]
            grafico.scatter(x_aa, y_aa, z_aa, s=t_aa, color=cor_aa)

    # Plotar os átomos da molécula ligante no gráfico
    if ver_ml:
        for atomo_ml in atomos_molecula:
            x_ml = atomo_ml[coord_x]
            y_ml = atomo_ml[coord_y]
            z_ml = atomo_ml[coord_z]
            grafico.scatter(x_ml, y_ml, z_ml, s=t_ml, color=cor_ml)

    # Identificar os eixos do gráfico
    grafico.set_xlabel('Eixo X (Å)')
    grafico.set_ylabel('Eixo Y (Å)')
    grafico.set_zlabel('Eixo Z (Å)')

    # Mostrar o gráfico
    plt.show()
    
