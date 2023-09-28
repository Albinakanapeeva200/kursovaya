import json
import os.path

file_dict = os.path.join('operations.json')

with open(file_dict, 'r', encoding='utf-8') as file:
    file_ = json.load(file)

    
def account_num_mask(number_to):
    account_num_masked = '*' * len(number_to[-6:-4]) + number_to[-4:]
    return account_num_masked


def card_num_mask(number_from):
    card_num_masked = number_from[0:4] + ' ' + number_from[4:6] + '*' * len(number_from[6:-4]) + number_from[-4:]
    return card_num_masked
