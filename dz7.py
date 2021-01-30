#dz7
import json
with open('dz7.txt') as f_obj:

    count_el = 0
    everage_num = 0
    my_list = []
    dict_profit = {}
    dict_looser = {}

    for f_str in f_obj:
        sp_str = f_str.split()
        if (int(sp_str[2]) - int(sp_str[3])) > 0:
            count_el = count_el + 1
            dict_el = {sp_str[0]: int(sp_str[2]) - int(sp_str[3])}
            everage_num = (everage_num + int(sp_str[2]) - int(sp_str[3]))
            list_el = dict_profit.update(dict_el)

        if (int(sp_str[2]) - int(sp_str[3])) < 0:
            dict_el = {sp_str[0]: int(sp_str[2]) - int(sp_str[3])}
            list_el_l = dict_looser.update(dict_el)

    my_list.append(dict_profit)
    my_list.append({'average_profit': int(everage_num / count_el)})
    print(my_list)

with open('dz7.json', 'w') as json_f:
    json.dump(my_list, json_f)