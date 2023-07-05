
def reverse_phrase(phrase):
    words = phrase.split(' ') # junta cada palavra em uma lista

    reversed_sentence = ' '.join(reversed(words)) # Junta cada item da lista criada em uma string,  
    # usando o método reversed que faz isso detrás pra frente

    return reversed_sentence


a = 'Hello, world! OpenAI is amazing.'

print(reverse_phrase(a))

    
