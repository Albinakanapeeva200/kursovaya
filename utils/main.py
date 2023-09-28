import json
import os.path
import datetime
from all_funct import account_num_mask, card_num_mask

file_dict = os.path.join('operations.json')

with open(file_dict, 'r', encoding='utf-8') as file:
    file_ = json.load(file)


def operation_output():
    """ функция вывода операций"""
    sort_operations_state = [sort_operations_state for sort_operations_state in file_ if sort_operations_state.get('state') == 'EXECUTED']
    sort_operations_date = sort_operations_state.sort(key=lambda x: x.get('date'), reverse=True)
    for i in sort_operations_state[:5]:
        date_time = i['date']
        date_ = datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S.%f")
        print(f"{date_.date().strftime('%Y.%m.%d')} {i['description']}")
        if 'from' not in i:
            card = i['to'].split()
            number_to = card[-1]
            num_to = account_num_mask(number_to)
            print(f" > {' '.join(card[:-1])} {num_to}")
        else:
            card = i['to'].split()
            number_to = card[-1]
            num_to = account_num_mask(number_to)
            card_ = i['from'].split()
            number_from = card_[-1]
            num_from = card_num_mask(number_from)
            print(f"{' '.join(card_[:-1])} {num_from} > {' '.join(card[:-1])} {num_to}")

        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print(" ")


#operation_output()
