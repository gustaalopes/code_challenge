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