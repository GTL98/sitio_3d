# Sítio 3D

O *software* **Sítio 3D** é um programa feito em Python que consiste em mostrar a estrutura tridimensional do sítio de ligação de proteínas. A visualização ocorre em gráficos de três dimensões onde cada átomo dos aminoácidos do sítio de ligação e a molécula ligante são dispostas como pontos. Os pontos que representam os aminoácidos são coloridos conforme o seu grupo químico: básico no espectro do azul, ácido no espectro do vermelho, polares no espectro do verde e apolares no espectro do violeta/rosa. A molécula ligante, por sua vez, está na cor preta.

### Requerimentos
    - math
    - matplotlib
    
### Como usar o Sítio 3D?

O arquivo usado para que o programa funcione é o `main.py`. Para visualizar a plotagem basta passa o path (relativo ou absoluto) do arquivo PDB, informar a cadeia de aminoácidos a ser analisada, qual é a molécula ligante desejada, a distância que os átomos do aminoácido devem estar da molécula e se deseja visualizar o sítio com a molécula ou não.

### Visualização

Para visualizar a plotagem basta selecionar o tamanho dos pontos e se deseja que seja plotada a molécula ligante junto com o sítio ou somente os aminoácidos. Além disso, há uma legenda de cor no canto superior esquerdo informando qual cor representa qual aminoácido. Vejamos alguns exemplos:

**Sítio de ligação + molécula ligante (5gwz.pdb)**:

![figura_1](https://user-images.githubusercontent.com/91161693/163223075-1094ec89-bcad-433a-9f4b-d9990718f21e.png)


**Sítio de ligação (5gwz.pdb)**:

![figura_2](https://user-images.githubusercontent.com/91161693/163223351-be5b6e06-16b0-49d9-9fdf-569eddfc28f8.png)


### Objetivo

O objetivo do **Sítio 3D** é visualizar de maneira rápida como é o formato tridimensional do sítio de ligação de proteínas ou quais são os aminoácidos pertencentes a esse sítio, o que fornece uma informação a mais sobre a característica da molécula ligante e possivelmente da enzima. Esse *software* é somente um estudo, não servindo como base para comprovação de dados.

Sei que tem muito o que melhorar neste programa, mas já é um começo!
