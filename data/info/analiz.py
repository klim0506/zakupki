import pandas
import pymorphy2

data = pandas.read_csv('/small_data/small_data/Контракты 44ФЗ.csv', sep=';')

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
