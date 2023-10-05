import json
import datetime


def load_operations(file_dict):
    """Функция читает файл json"""
    with open(file_dict, 'r', encoding='utf-8') as file:
        file_ = json.load(file)
        return file_


def get_executed_operations(file_):
    """Функция сортирует статус перевода"""
    sort_operations_state = [sort_operations_state for sort_operations_state in file_ if
                             sort_operations_state.get('state') == 'EXECUTED']
    return sort_operations_state


def sort_operations_by_date(sort_operations_state):
    """Функция сортирует даты"""
    sort_operations_state.sort(key=lambda x: x.get('date'), reverse=True)
    return sort_operations_state


def get_last_operations(file_):
    """Функция получает последние выполненные операции"""
    sort_operations_state = get_executed_operations(file_)
    sort_operations = sort_operations_by_date(sort_operations_state)
    return sort_operations[:5]


def account_num_mask(number_to):
    """ функция маскирует номер счета"""
    account_num_masked = '*' * len(number_to[-6:-4]) + number_to[-4:]
    return account_num_masked


def card_num_mask(number_from):
    """ функция маскирует номер карты"""
    card_num_masked = number_from[:4] + ' ' + number_from[4:6] + '*' * len(number_from[-10:-4]) + number_from[-4:]
    return card_num_masked


def get_valid_operation_obj(sort_operations):
    """ функция вывода операций"""
    for i in sort_operations:
        date_ = datetime.datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime('%Y.%m.%d')
        description = i['description']
        print(f'{date_} {description}')
        if 'from' not in i:
            card = i['to'].split()
            number_to = card[-1]
            num_to = account_num_mask(number_to)
            print(f" > {' '.join(card[:-1])} {num_to}")
        elif 'Счет' in i['from']:
            card = i['to'].split()
            number_to = card[-1]
            num_to = account_num_mask(number_to)
            card_ = i['from'].split()
            number_from = card_[-1]
            num_from = account_num_mask(number_from)
            print(f"{' '.join(card_[:-1])} {num_from} -> {' '.join(card[:-1])} {num_to}")
        else:
            card = i['to'].split()
            number_to = card[-1]
            num_to = account_num_mask(number_to)
            card_ = i['from'].split()
            number_from = card_[-1]
            num_from = card_num_mask(number_from)
            print(f"{' '.join(card_[:-1])} {num_from} -> {' '.join(card[:-1])} {num_to}")

        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
        print(" ")
