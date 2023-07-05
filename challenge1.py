from collections import Counter
import re

'''
1) Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:
'''


def reverse_phrase(phrase):
    words = phrase.split(' ')  # junta cada palavra em uma lista, usando como separador para identificação dos items o espaço (' ')

    # Junta cada item da lista criada em uma string,
    reversed_sentence = ' '.join(reversed(words))
    # usando o método reversed que faz isso de trás pra frente

    return reversed_sentence


a = 'Hello, world! OpenAI is amazing.'

print(reverse_phrase(a))

'''
2) Remova todos os caracteres duplicados na string abaixo:
'''


def remove_duplicates(phrase):
    new_phrase = ''  # variável que vai receber os caracteres que não forem repetidos
    for char in phrase:  # loop para iterar sobre a frase oferecida
        if char not in new_phrase:  # condicional para verificar se não há ainda o caractere na nova variável
            new_phrase += char  # concatenação
    return new_phrase


phrase = 'Hello, World!'

no_duplicate = remove_duplicates(phrase)

print(no_duplicate)


'''
3) Encontre a substring palindroma mais longa na string abaixo:
'''

def sub_palindrome(string):
    palindrome = ''
    lenght = len(string)
    for i in range(lenght): # loop que itera sobre o tamanho da palavra fornecida
        for j in range(i+1, lenght+1): #loop que itera sobre o tamanho restrito da palavra fornecida
            substring = string[i:j] #variável que recebe o tamanho restrito da palavra fornecida
            if substring == substring[::-1]: #condicional: checa se variável = de trás pra frente, confirma que é palíndromo
                if len(substring) > len(palindrome): # condicional para verificar se o palíndromo atual é maior que o último verificado
                    palindrome = substring
    return palindrome


a = 'babad'

print(sub_palindrome(a))

'''
4) Coloque em maiúscula a primeira letra de cada frase na string:
'''

# Usando o módulo regular expressions 'import re'
def capitalize_first(string):
    capitalized_sentence = ''
    li = re.split(r'(?<=[.!?])\s', string) # Delimitando os caracteres de pontuação e criando a lista que vai armazenar cada frase

    capitalized_list = []
    for i in range(0, len(li)):
        capitalized_list.append(li[i].capitalize()) # Tornando maiúscula cada frase separada e armazenando numa lista

    capitalized_sentence = ' '.join(capitalized_list) # Juntando as frases da lista criada anteriormente
    return capitalized_sentence


a = "hello. how are you? i'm fine, thank you."
print(capitalize_first(a))


'''
5) Verifique se a string é um anagrama de um palíndromo:
'''
# Utilizando o módulo counter que conta valores e cria um dicionário a partir disso

def anagram_palindrome(string):
    char_values = Counter(string) #transformando a string em um dicionário com a quantidade de cada letra estabelecida
    odd_count = 0 # Quantidade de caracteres ímpares na string
    for odd in char_values.values(): # checa quantidade de cada caractere. Se for impar a contagem sobe +1
        if odd % 2 != 0:
            odd_count += 1
    return odd_count <= 1 # Retorna True para anagrama de um palíndromo se a contagem de caracteres ímpares seja = ou < que 1

string = 'racecar'
print(anagram_palindrome(string))