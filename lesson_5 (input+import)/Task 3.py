import random
input_str = input("Please, enter any string: ")
str_length = len(input_str)
for i in range(5):
    char_list = list(input_str)
    random.shuffle(char_list)
    new_str = ''.join(char_list)
    print(new_str)