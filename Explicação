Este código é um jogo da forca em Python. Ele permite que o jogador escolha um tema (como animais, países, filmes, séries, etc.)
e tenta adivinhar a palavra oculta escolhida aleatoriamente pelo programa. Abaixo, vou explicar cada parte do código:

Bibliotecas Importadas:
random: Utilizado para gerar números aleatórios.
unidecode: Utilizado para remover acentos e caracteres especiais das palavras.

Apresentação do jogo com destaque visual:
print('\033[1;30;107mBEM VINDO AO JOGO DA FORCA!\033[m')
print('-=' * 15)

Obtenção do Nome do Jogador:
nome = str(input('Diga-nos qual o seu nome: '))
print('-=' * 15)

Escolha de Tema:
print(f'Seja bem vindo \033[1m{nome}\033[m!')
print('')
print('''Escolha 1 de nossos temas: ...''')
escolha = int(input('Sua Escolha: '))
print('-=' * 15)

Apresenta uma lista de temas para o jogador escolher.

Seleção de Palavra Oculta com Base na Escolha do Tema:
if escolha == 1:
    # ... Código para o tema 'Animais'
elif escolha == 2:
    # ... Código para o tema 'Países'
elif escolha == 3:
    # ... Código para o tema 'Filmes'
# ... (repetido para outros temas)

Para cada escolha de tema, há um bloco de código correspondente que define uma lista de palavras e inicia o jogo da forca com base nesse tema.
    
Lógica do Jogo da Forca:
Para cada tema, há um código semelhante que inclui:
- Seleção aleatória de uma palavra oculta do tema.
- Inicialização da palavra oculta com espaços em branco.
- Loop principal para as tentativas do jogador.
- Verificação de acertos e erros.
- Exibição da palavra oculta atualizada.
- Mensagem de vitória ou derrota no final.
    
Visualização Colorida no Terminal:
O uso de códigos de escape ANSI (por exemplo, \033[1;92m) é para adicionar cor ao texto no terminal. Isso é comumente usado para dar destaque às mensagens de saída.
