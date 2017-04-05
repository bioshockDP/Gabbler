from src.server_utils.db_utils import count_words
from src.server_utils.parser import get_words


# return the most probable answer
def get_answer(data):
    words = get_words(data)
    account_count = count_words('account', words)
    promotions_count = count_words('promotions', words)
    stores_count = count_words('stores', words)
    max_count = max(account_count, promotions_count, stores_count)

    answer = "(слова не співпали)(звязать з оператором)"
    if max_count == 0:
        return answer
    if account_count == max_count:
        answer = account_answer()
    elif promotions_count == max_count:
        answer = promotions_answer()
    elif stores_count == max_count:
        answer = stores_answer()
    return answer


# return answer about account
def account_answer():
    money = 0
    answer = "На Вашем счету {} грн. Спросите меня ещё о чем-то.".format(money)

    return answer


# return answer about promotions
def promotions_answer():
    promotions = ["акция-1", "акция-2", "акция-3"]

    if promotions.__len__() == 0:
        return 'Сейчас нет акционых предложений...'

    answer = "Акции действующие в даный момент:"
    for promotion in promotions:
        answer += '\n->' + promotion
    return answer


# return answer about store
def stores_answer():
    address = "(якась адреса)"
    answer = "Спасибо за вопрос! Вы можете приехать в ближайший наш магазин,который находиться по адрессу: {}".format(
        address)

    return answer

