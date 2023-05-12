def count_w(sentence):
    words = sentence.split()
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    return dict_words
sentence = input("Enter any sentence: ")
print("Sentence:", sentence)
word_count = count_w(sentence)
print("Word count:", word_count)


