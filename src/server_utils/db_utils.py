from mysql.connector import MySQLConnection, Error
from src.server_utils.db_config import read_db_config
from src.server_utils.parser import get_item


def get_cursor():
    """Return connection and cursor"""
    db_config = read_db_config()
    conn = MySQLConnection(**db_config)
    return conn, conn.cursor()


def count_words(table_name, word_list):
    """Return the amount of words that match"""

    count = 0
    try:
        connection, cursor = get_cursor()
        cursor.execute("select name from gubbler.{0}".format(table_name))
        row = cursor.fetchone()

        # comparing words in message and data base
        while row is not None:
            for word in word_list:
                if get_item(row) == word:
                    count += 1

            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        connection.close()
        return count
