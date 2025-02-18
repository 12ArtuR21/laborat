# Четные четырехричные числа, не превышающие 204710, у которых вторая справа цифра равна 1. Выводит на экран цифры числа, исключая единицы. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
with open("chisla.txt", "w") as fd:
    for element in range (1000, 2048):
        fd.write(str(element) + '\n')

with open('chisla.txt') as fd:
    file = fd.read().split()
print(*file)

WORDS_ONES = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']

def num_to_word(sr_num):
        return WORDS_ONES[sr_num]

def sr_num(list):
    list.sort()
    sr = (int(list[0]) + int(list[2])) // 2
    return sr

for element in file:
    string_element = str(element)
    if int(element) % 2 == 0 and string_element[2] == '1':
        spisok = [string_element[0], string_element[1], string_element[3]]
        print(element, '. Цифры числа: ', *spisok, '. Среднее число между минимальным и максимальным: ', sr_num(spisok),' (',num_to_word(sr_num(spisok)), ')', sep="")
