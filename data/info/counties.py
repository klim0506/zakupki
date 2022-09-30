def county_range(data_list):  # ранжирует страны по упомянаемсти в данных
    my_lib = {}
    for i in list(data_list):
        try:
            for j in i.split('|'):
                if j not in my_lib:
                    my_lib[j] = 0
                my_lib[j] += 1

        except Exception:
            pass

    return [i[0] for i in sorted(my_lib.items(), key=lambda x: x[1], reverse=True)]  # list id стран в порядке убывания
