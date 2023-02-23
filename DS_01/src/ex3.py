import string

def MostUsedWord(bookPath, stopWordPath):
    book = open(bookPath, 'r')
    list_of_book = book.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
    stop_bdsm_words = open(stopWordPath, 'r')
    list_stop_bdsm_words = stop_bdsm_words.read().split()
    new_list_of_book = []
    for i in list_of_book: # Удаление стоп-слов из списка
        presence_flag = 0
        for j in list_stop_bdsm_words:
            if (i == j):
                presence_flag = 1
        if(not(presence_flag)):
            new_list_of_book.append(i)
    dict_of_book = {}
    for i in new_list_of_book:
        if i.isalpha() and len(i) > 4:  # слово не число длинна слова не меньше 4
            dict_of_book[i] = dict_of_book.get(i, 0) + 1

    sorted_dict_of_book = sorted(dict_of_book.items(), key=lambda x: x[1], reverse = True)
    final_dict = dict(sorted_dict_of_book)
    return list(final_dict.keys())[0]

bookPath = "../datasets/war_and_peace.txt"
stopWordPath = "../datasets/stop_words_russian.txt"
print(MostUsedWord(bookPath, stopWordPath))