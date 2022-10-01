import pandas
import pymorphy2


def parsing_names(path):
    data = pandas.read_csv(path, sep=';')

    data['root_words'] = ''

    shcet = 0
    morphy = pymorphy2.MorphAnalyzer()

    for i in list(data.product_name):
        stroca = ''
        for j in i.split():
            j = morphy.parse(j)[0]
            stroca += j.normal_form + ' '

        data.root_words[shcet] = stroca
        shcet += 1

    return 0


def parsing_zapros(string):
    parser = pymorphy2.MorphAnalyzer(lang='ru')

    zapros_param = {'NOUN': [], 'ADJF': [], 'ELSE': []}

    for i in string.split():
        chast_rechi = parser.parse(i)[0].tag.POS

        if chast_rechi == 'PRTF':
            zapros_param['ADJF'].append(i)
        elif chast_rechi != 'NOUN' and chast_rechi != 'ADJF':
            zapros_param['ELSE'].append(i)
        else:
            zapros_param[chast_rechi].append(i)

    return zapros_param
