from collections import Counter
import re

'''
1) Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:
'''


def reverse_phrase(phrase):
    # junta cada palavra em uma lista, usando como separador para identificação dos items o espaço (' ')
    words = phrase.split(' ')

    # Junta cada item da lista criada em uma string,
    reversed_sentence = ' '.join(reversed(words))
    # usando o método reversed que faz isso de trás pra frente

    return reversed_sentence


print('----- Execução do desafio 1 -----')
print('')
a = 'Hello, world! OpenAI is amazing.'
print('Teste 1: ', a)
print('Output teste 1: ', reverse_phrase(a))
b = 'Omg, this phrase is reversed!'
print('Teste 2: ', b)
print('Output teste 2: ', reverse_phrase(b))
c = 'Estou muito empolgado com este desafio!'
print('Teste 3: ', c)
print('Output teste 3: ', reverse_phrase(c))
print('')
print('---------- Fim do desafio 1 ----------')

print('')

'''
2) Remova todos os caracteres duplicados na string abaixo:
'''


def remove_duplicates(phrase):
    new_phrase = ''  # variável que vai receber os caracteres que não forem repetidos
    for char in phrase:  # loop para iterar sobre a frase oferecida
        if char not in new_phrase:  # condicional para verificar se não há ainda o caractere na nova variável
            new_phrase += char  # concatenação
    return new_phrase


print('----- Execução do desafio 2 -----')
print('')
a = 'Hello, World!'
print('Teste 1: ', a)
print('Output teste 1: ', remove_duplicates(a))
b = 'Goodbye horses'
print('Teste 2: ', b)
print('Output teste 2: ', remove_duplicates(b))
c = 'Merci beaucoup!'
print('Teste 3: ', c)
print('Output teste 3: ', remove_duplicates(c))
print('')
print('---------- Fim do desafio 2 ----------')

print('')

'''
3) Encontre a substring palindroma mais longa na string abaixo:
'''


def sub_palindrome(string):
    palindrome = ''
    lenght = len(string)
    for i in range(lenght):  # loop que itera sobre o tamanho da palavra fornecida
        # loop que itera sobre o tamanho restrito da palavra fornecida
        for j in range(i+1, lenght+1):
            # variável que recebe o tamanho restrito da palavra fornecida
            substring = string[i:j]
            # condicional: checa se variável = de trás pra frente, confirma que é palíndromo
            if substring == substring[::-1]:
                # condicional para verificar se o palíndromo atual é maior que o último verificado
                if len(substring) > len(palindrome):
                    palindrome = substring
    return palindrome


print('----- Execução do desafio 3 -----')
print('')
a = 'babad'
print('Teste 1: ', a)
print('Output teste 1: ', sub_palindrome(a))
b = 'bobobao'
print('Teste 2: ', b)
print('Output teste 2: ', sub_palindrome(b))
c = 'radares'
print('Teste 3: ', c)
print('Output teste 3: ', sub_palindrome(c))
print('')
print('---------- Fim do desafio 3 ----------')
print('')

'''
4) Coloque em maiúscula a primeira letra de cada frase na string:
'''

# Usando o módulo regular expressions 'import re'


def capitalize_first(string):
    capitalized_sentence = ''
    # Delimitando os caracteres de pontuação e criando a lista que vai armazenar cada frase
    li = re.split(r'(?<=[.!?])\s', string)

    capitalized_list = []
    for i in range(0, len(li)):
        # Tornando maiúscula cada frase separada e armazenando numa lista
        capitalized_list.append(li[i].capitalize())

    # Juntando as frases da lista criada anteriormente
    capitalized_sentence = ' '.join(capitalized_list)
    return capitalized_sentence


print('----- Execução do desafio 4 -----')
print('')
a = "hello. how are you? i'm fine, thank you."
print('Teste 1: ', a)
print('Output teste 1: ', capitalize_first(a))
b = 'omg! someone capitalize this! urgent.'
print('Teste 2: ', b)
print('Output teste 2: ', capitalize_first(b))
c = 'na internet? pontuação correta e letra maiúscula é raridade!'
print('Teste 3: ', c)
print('Output teste 3: ', capitalize_first(c))
print('')
print('---------- Fim do desafio 4 ----------')
print('')

'''
5) Verifique se a string é um anagrama de um palíndromo:
'''
# Utilizando o módulo counter que conta valores e cria um dicionário a partir disso


def anagram_palindrome(string):
    # transformando a string em um dicionário com a quantidade de cada letra estabelecida
    char_values = Counter(string)
    odd_count = 0  # Quantidade de caracteres ímpares na string
    for odd in char_values.values():  # checa quantidade de cada caractere. Se for impar a contagem sobe +1
        if odd % 2 != 0:
            odd_count += 1
    # Retorna True para anagrama de um palíndromo se a contagem de caracteres ímpares seja = ou < que 1
    return odd_count <= 1


print('----- Execução do desafio 5 -----')
print('')
a = 'racecar'
print('Teste 1: ', a)
print('Output teste 1: ', anagram_palindrome(a))
b = 'anagram'
print('Teste 2: ', b)
print('Output teste 2: ', anagram_palindrome(b))
c = 'bombom'
print('Teste 3: ', c)
print('Output teste 3: ', anagram_palindrome(c))
print('')
print('---------- Fim do desafio 5 ----------')

input('Pressione enter para fechar a aplicação.')
