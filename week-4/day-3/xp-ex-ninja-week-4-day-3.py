def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

sentence = "You have entered a wrong domain"
print(reverse_sentence(sentence))
