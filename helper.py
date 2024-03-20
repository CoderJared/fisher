"""
  Create By Jared on 
"""
__author__ = "Jared"


def is_isbn_or_key(word):
    """
    Checks is isbn or not
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isnumeric():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if ('-' in word and len(short_word) == 10 and short_word
            .isnumeric()):
        isbn_or_key = 'isbn'
    return isbn_or_key
