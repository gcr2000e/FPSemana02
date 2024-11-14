#função para contagem de caractéres e dicionário
def char_count(sentence):
    count = {}

    for i in sentence:
        if i.isalpha():
         if i in count:
            count[i] += 1
         else:
            count[i] = 1

    return count

#input da frase
sentence = input()

#output
output = char_count(sentence)
print(output)
