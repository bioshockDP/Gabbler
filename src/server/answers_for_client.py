from src.data_base.mysql_connection import *


def get_answer(data):
    words = get_words(data)
    count_1 = count_words('table_1', words)
    count_2 = count_words('table_2', words)
    count_3 = count_words('table_3', words)
    max_count = max(count_1, count_2, count_3)

    answer = "Вибачте, я не можу відповісти на Ваше запитання. Зв'язати Вас з " \
             "оператором?"
    if count_1 == max_count:
        answer = answer_1()
    elif count_2 == max_count:
        answer = answer_2()
    elif count_3 == max_count:
        answer = answer_3()
    return answer


def answer_1():
    return "answer 1"


def answer_2():
    return "answer 2"


def answer_3():
    return "answer 3"
