from utils.all_funct import account_num_mask, card_num_mask


def test_account_num_mask():
    number_to = '14211924144426031657'
    result_to = '**1657'
    assert account_num_mask(number_to) == result_to


def test_card_num_mask():
    number_from = '1246377376343588'
    result_from = '1246 37******3588'
    assert card_num_mask(number_from) == result_from
