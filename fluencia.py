# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import utils


def distinguish_words(trans):
    # função para separar uma frase em palavra por palavra
    j = 0  # apenas um incrementador
    first_read = []  # variavel onde será salvo a frase
    for i in range(len(trans.results)):
        first_read.append(trans.results[i].alternatives[0].transcript)
    # print(first_read)
    mid_word = [[]]  # variavel para montar as palavras reconhecidas
    for x in range(len(first_read)):  # loop pra olhar quantas frases tem
        for k in range(len(first_read[x])):  # loop pra olhar cada caracter da frase
            if ' ' not in first_read[x][k]:
                mid_word[j] += first_read[x][k]  # adiciona cada caracter da palavra
            else:
                j += 1  # incrementa o incrementador
                mid_word.append([])  # cria um espaço para próxima palavra
    # print(mid_word)
    word = []  # variavel para juntar os caracteres e formar a palavra

    for u in range(len(mid_word)):
        word.append([])  # cria o espaço da palavra
        word[u] = ''.join(mid_word[u])  # junta os caracteres e forma a palavra
    # print(word)

    # as linhas abaixo são necessárias pra rodar no python 2
    # for l in range(len(word)):  # loop para mudar o código das palavras
    #     word[l] = word[l].encode('utf-8')  # código pra aceitar ç e acentos
        # print(word[l])
    return word


def fluencia(words):
    # função para realizar a pontuação do teste, o número de animais reconhecidos
    rec_animals = []  # lista para indicar os animais ja reconhecidos
    score = 0
    # print(words)
    h = 0  # variavel auxiliar
    while h < len(words):
        temp = ''  # variavel onde vai se combinar as strings
        no_match = 1  # variavel de controle de loop
        lastword = 0
        while no_match == 1:  # loop pra testar tds as possibilidades
            for u in range(h, len(words) - lastword):  # combina as strings para testar
                if u == h:
                    temp = words[u]
                else:
                    temp = temp + '-' + words[u]
            # print(temp, lastword)

            for s in utils.list_animals:  # loop para verificar tds os animais da lista
                # print(s, temp)
                if len(temp) == len(s):  # verifica o tamanho das strings
                    # print('mesmo tamanho')
                    if temp in s:  # verifica se eh um animal
                        # print('aaaaa', temp)
                        if s not in rec_animals:  # elimina animais repetidos
                            rec_animals.append(s)
                            score += 1
                            no_match = 0
                            print(score, s, temp)
                            if len(words) - lastword - h >= 2:  # em caso do animal hifado, aumenta o step no prx animal
                                h += len(words) - lastword - h
                            else:
                                h += 1
                            break  # tds os breaks são para quebrar o loop for
                        else:
                            if len(words) - lastword - h >= 2:  # em caso do animal hifado, aumenta o step no prx animal
                                h += len(words) - lastword - h
                            else:
                                h += 1
                            lastword += 1
                            no_match = 0
                            break
                    elif temp[:-1] in s:  # elimina animais com semantica semelhantes
                        if s not in rec_animals:
                            rec_animals.append(s)
                            no_match = 0
                            score += 1
                            print(score, s, temp, 'aaaaaaa')
                            h += 1
                            break
                        else:
                            lastword += 1
                            h += 1
                            no_match = 0
                            break
                if s == 'umbrella':  # nao houve match com a combinacao, muda a combinacao pra nova tentativa
                    lastword += 1
            if lastword + h == len(words) and no_match == 1:  # deixou apenas a ultima string e nao teve match, a string nao eh animal e segue
                no_match = 0
                h += 1

    return score, rec_animals
