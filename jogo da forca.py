import random
from unidecode import unidecode

print('\033[1;30;107mBEM VINDO AO JOGO DA FORCA!\033[m')
print('-=' * 15)

nome = str(input('Diga-nos qual o seu nome: '))
print('-=' * 15)

print(f'Seja bem vindo \033[1m{nome}\033[m!')
print('')

print('''Escolha 1 de nossos temas:
\033[1;91m[1]\033[m - \033[1;92mAnimais\033[m
\033[1;91m[2]\033[m - \033[1;92mPaíses\033[m
\033[1;91m[3]\033[m - \033[1;92mFilmes\033[m
\033[1;91m[4]\033[m - \033[1;92mSéries\033[m
\033[1;91m[5]\033[m - \033[1;92mPersonagens da Ficção\033[m
\033[1;91m[6]\033[m - \033[1;92mPersonagens Históricos\033[m
\033[1;91m[7]\033[m - \033[1;92mAnimes (Títulos)\033[m
\033[1;91m[8]\033[m - \033[1;92mTecnologia\033[m
\033[1;91m[9]\033[m - \033[1;92mPartes do corpo humano\033[m
\033[1;91m[10]\033[m - \033[1;92mObjetos de dentro de casa\033[m''')
escolha = int(input('Sua Escolha: '))
print('-=' * 15)



#ANIMAIS
if escolha == 1:
    animais = ['tigre', 'girafa', 'urso', 'jacaré', 'pinguim', 'canguru', 'golfinho', 'borboleta', 'rinoceronte', 'leopardo', 'coelho', 'tartaruga', 'águia', 'aranha', 'papagaio', 'caranguejo', 'morcego', 'coruja', 'gato', 'cachorro']

    #Escolher um animal aleatorio e remover acentos com o "unidecode"
    pc = unidecode(random.choice(animais))

    # Obter o número de letras na palavra escolhida
    letras = len(pc)

    # Inicializa a palavra oculta com espaços em branco representando cada letra e depois a exibe na tela
    palavraOculta = ['_'] * letras
    print('\033[1mJá escolhi um animal!\033[m')
    print('Animal Escolhido: ', ' '.join(palavraOculta))

    print('-=' * 15)

    # Lista para armazenar as posições onde a letra aparece
    posicoes = []

    # Limite de tentativas
    limiteTentativas = 6
    tentativas = 0 #contador

    # Loop enquanto a palavra oculta ainda contiver espaços em branco e o número de tentativas for menor que o limite
    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ')).lower().strip())
        print('-=' * 15)

        # Reinicializa a lista de posições para cada chute
        posicoes = []

        # Verificando cada posição na palavra
        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i) # Adiciona a posição "i" à lista posicoes. Isso significa que a letra "chute" foi encontrada na posição "i" da palavra.
                palavraOculta[i] = chute # Substitui o "espaço em branco" (_) pelo chute na palavra oculta

        # Informações
        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'\033[1;91mA letra "{chute}" não está correta!\033[m')
            tentativas += 1 #Incrementa o numero de tentativas

        # Exibindo a palavra oculta atualizada
        print('Animal Escolhido: ', ' '.join(palavraOculta))

    # Verificando se o usuário venceu ou perdeu
    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m O animal era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[1;91mVocê PERDEU!\033[m O animal era: {pc.title()}')



#PAÍSES
elif escolha == 2:
    paises = ['brasil', 'canadá', 'japão', 'itália', 'méxico', 'frança', 'rússia', 'alemanha', 'índia', 'austrália', 'china', 'argentina', 'espanha', 'egito', 'nigéria', 'coreia do sul', 'áfrica do sul', 'turquia', 'suécia', 'tailândia']
    pc = unidecode(random.choice(paises))
    letras = len(pc)
    palavraOculta = []

    # Para colocar um espaço extra caso o filme tenha 2 ou+ mais palavras separadas
    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi um país!\033[m')
    print('País Escolhido: ', ' '.join(palavraOculta))

    print('-=' * 15)

    posicoes = []

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ')).lower().strip())
        print('-=' * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'\033[1;91mA letra "{chute}" não está correta!\033[m')
            tentativas += 1

        print('País Escolhido: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m O país era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[mVocê PERDEU!\033[m O país era: {pc.title()}')



#FILMES
elif escolha == 3:
    filmes = ['avatar', 'titanic', 'o poderoso chefão', 'o senhor dos anéis', 'jurassic park', 'os vingadores', 'o rei leão', 'bad boys', 'star wars', 'matrix', 'forrest gump', 'o exorcista', 'o silêncio dos inocentes', 'tubarão', 'indiana jones', 'casablanca', 'clube da luta', 'gladiador', 'cidade de deus', 'indiana jones']
    pc = unidecode(random.choice(filmes))

    letras = len(pc)
    palavraOculta = []

    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi um filme!\033[m')
    print('Filme Escolhido: ', ' '.join(palavraOculta))

    print('-=' * 15)

    posicoes = []

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ').lower().strip()))
        print('-=' * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'\033[1;91mA letra "{chute}" não está correta!\033[m')
            tentativas += 1

        print('Filme Escolhido: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m O filme era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[1;91mVocê PERDEU!\033[m O filme era: {pc.title()}')



#SÉRIES
elif escolha == 4:
    series = ['friends', 'stranger things', 'game of thrones', 'breaking bad', 'the walking dead', 'grey\'s anatomy', 'la casa de papel', 'the office', 'black mirror', 'vikings', 'the big bang theory', 'narcos', 'peaky blinders', 'how i met your mother', 'supernatural', 'the simpsons', 'sons of anarchy', 'house of cards', 'the crown', 'the witcher']
    pc = unidecode(random.choice(series))

    letras = len(pc)
    palavraOculta = []

    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi uma série!\033[m')
    print('Série Escolhida: ', ' '.join(palavraOculta))
    print('-=' * 15)

    posicoes=[]

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ').lower().strip()))
        print('-=' * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'\033[1;91mA letra "{chute}" não está correta!\033[m')
            tentativas += 1

        print('Série Escolhida: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m A série era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[1;91mVocê PERDEU!\033[m A série era: {pc.title()}')



#Personagens da Ficção
elif escolha == 5:
    personagens = ['superman', 'sherlock holmes', 'mickey mouse', 'katniss everdeen', 'hannibal lecter', 'aragorn', 'darth vader', 'wonder woman', 'tarzan', 'gandalf', 'spider man', 'hermione granger', 'pikachu', 'drácula', 'mulher maravilha', 'batman', 'james bond', 'gollum', 'popeye', 'harry potter']
    pc = unidecode(random.choice(personagens))

    letras = len(pc)
    palavraOculta = []

    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi um personagem!\033[m')
    print('Personagem Escolhido(a): ', ' '.join(palavraOculta))
    print('-=' * 15)

    posicoes = []

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ').lower().strip()))
        print('-=' * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[1;92m')
        else:
            print(f'\033[1;91mA letra "{chute}" não está correta!\033[m')
            tentativas += 1

        print('Personagem Escolhido: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabens! \033[1;92mVocê GANHOU!\033[m O(a) personagem era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[1;91mVocê PERDEU!\033[m O(a) personagem era: {pc.title()}')



#Personagens Históricos
elif escolha == 6:
    personagens = ['cleopatra', 'napoleao bonaparte', 'albert einstein', 'leonardo da vinci', 'joana darc', 'martin luther king jr', 'mahatma gandhi', 'marie curie', 'william shakespeare', 'anne frank', 'isaac newton', 'frida kahlo', 'winston churchill', 'amelia earhart', 'rosa parks', 'che guevara', 'galileu galilei', 'genghis khan', 'julio cesar', 'nelson mandela']
    pc = unidecode(random.choice(personagens))

    letras = len(pc)
    palavraOculta = []

    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi uma Pessoa!\033[m')
    print('Pessoa Escolhida: ', ' '.join(palavraOculta))
    print('-=' * 15)

    posicoes = []

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ')).lower().strip())
        print('-=' * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'\033[mA letra "{chute}" não está correta!\033[m')
            tentativas += 1

        print('Pessoa Escolhida: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m A pessoa era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[1;91mVocê PERDEU!\033[m A pessoa era: {pc.title()}')



#Animes
elif escolha == 7:
    animes = ['naruto', 'bleach', 'one piece', 'dragon ball', 'attack on titan', 'death note', 'fullmetal alchemist', 'fairy tail', 'hunter x hunter', 'sword art online', 'my hero academia', 'demon slayer', 'tokyo ghoul', 'cowboy bebop', 'neon genesis evangelion', 'one punch man', 'code geass', 'jojo\'s bizarre adventure', 'black clover', 'steins gate']
    pc = unidecode(random.choice(animes))

    letras = len(pc)
    palavraOculta = []

    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi um anime!\033[m')
    print('Anime Escolhido: ', ' '.join(palavraOculta))
    print('-=' * 15)

    posicoes = []

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ')).lower().strip())
        print('-=' * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'\033[1;91mA letra "{chute}" não está correta!\033[m')
            tentativas += 1

        print('Pessoa Escolhida: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m O anime era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[mVocê PERDEU!\033[m O anime era: {pc.title()}')



#Tecnologia
elif escolha == 8:
    tecnologia = ['computador', 'internet', 'smartphone', 'software', 'hardware', 'rede', 'programação', 'robótica', 'cibernética', 'inovação', 'nuvem', 'realidade virtual', 'inteligência artificial', 'blockchain', 'segurança', 'dados', 'sistemas', 'eletrônico', 'biometria', 'automação']
    pc = unidecode(random.choice(tecnologia))

    letras = len(pc)
    palavraOculta = []

    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi uma palavra!\033[m')
    print('Palavra Escolhida: ', ' '.join(palavraOculta))
    print('-=' * 15)

    posicoes = []

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ')).lower().strip())
        print("-=" * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'\033[1;91mA letra "{chute}" não está correta\033[m')
            tentativas += 1

        print('Palavra Escolhida: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m A palavra era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[1;91mVocê PERDEU!\033[m A palavra era: {pc.title()}')



#Partes do corpo humano
elif escolha == 9:
    corpoHumano = ['olhos', 'nariz', 'boca', 'orelhas', 'braços', 'pernas', 'cabelo', 'unhas', 'mãos', 'pés', 'língua', 'dentes', 'costas', 'pele', 'joelhos', 'cotovelos', 'pescoço', 'ombros', 'quadril', 'barriga']
    pc = unidecode(random.choice(corpoHumano))

    letras = len(pc)
    palavraOculta = []

    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi uma parte do corpo!\033[m')
    print('Parte Escolhida: ', ' '.join(palavraOculta))
    print('-=' * 15)

    posicoes = []

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ')).lower().strip())
        print('-=' * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'\033[1;91mA letra "{chute}" não está correta!\033[m')
            tentativas += 1

        print('Parte Escolhida: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m A parte do corpo humano era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[1;91mVocê PERDEU!\033[m A parte do corpo humano era: {pc.title()}')



#Objetos de dentro de casa
elif escolha == 10:
    casa = ['sofá', 'mesa', 'cadeira', 'geladeira', 'fogão', 'televisão', 'cama', 'armário', 'pia', 'lâmpada', 'quadro', 'tapete', 'espelho', 'janela', 'cortina', 'livro', 'computador', 'vaso', 'prateleira', 'relógio']
    pc = unidecode(random.choice(casa))

    letras = len(pc)
    palavraOculta = []

    for char in pc:
        if char == ' ':
            palavraOculta.append(' ')
        else:
            palavraOculta.append('_')

    print('\033[1mJá escolhi um objeto!\033[m')
    print('Objeto Escolhido: ', ' '.join(palavraOculta))
    print('-=' * 15)

    posicoes = []

    limiteTentativas = 6
    tentativas = 0

    while '_' in palavraOculta and tentativas < limiteTentativas:
        print(f'\033[1;91m(Você tem apenas 6 chances, se errar mais {tentativas - limiteTentativas}x, você perde!)\033[m')
        chute = unidecode(str(input('Chute uma letra: ')).lower().strip())
        print('-=' * 15)

        posicoes = []

        for i in range(letras):
            if pc[i] == chute:
                posicoes.append(i)
                palavraOculta[i] = chute

        if posicoes:
            print(f'\033[1;92mA letra "{chute}" está correta!\033[m')
        else:
            print(f'A letra "{chute}" não está correta!')
            tentativas += 1

        print('Objeto Escolhido: ', ' '.join(palavraOculta))

    if '_' not in palavraOculta:
        print(f'Parabéns! \033[1;92mVocê GANHOU!\033[m A parte do corpo humano era: {pc.title()}')
    else:
        print(f'Sinto muito! \033[1;91mVocê PERDEU!\033[m A parte do corpo humano era: {pc.title()}')