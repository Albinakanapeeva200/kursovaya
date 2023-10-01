import pytest
from utils.all_funct import (account_num_mask, card_num_mask, get_executed_operations, sort_operations_by_date,
                             get_last_operations)


@pytest.fixture
def file_():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }

        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }

        }
    ]


def test_get_executed_operations(file_):
    executed_operations = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }

        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }

        }
    ]
    result = get_executed_operations(file_)
    assert result == executed_operations


def test_sort_operations_by_date(file_):
    sort_operations_state = get_executed_operations(file_)
    executed_operations = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }

        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }

        }
    ]
    result = sort_operations_by_date(file_)
    assert result == executed_operations


def test_get_last_operations(file_):
    executed_operations = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            }

        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }

        }
    ]
    result = get_last_operations(file_)
    assert result == executed_operations


def test_account_num_mask():
    number_to = '14211924144426031657'
    result_to = '**1657'
    assert account_num_mask(number_to) == result_to


def test_card_num_mask():
    number_from = '1246377376343587'
    result_from = '1246 37******3587'
    assert card_num_mask(number_from) == result_from
