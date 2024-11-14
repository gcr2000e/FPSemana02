#function word_intersection
def word_intersection(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()

    set1 = set(words1)
    set2 = set(words2)

    intersection = set1 & set2

    output = [word for word in words1 if word in intersection]

    return ' '.join(output)

#sentences input
sentence1 = input()
sentence2 = input()

#output
print(word_intersection(sentence1, sentence2))