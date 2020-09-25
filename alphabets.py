# newStr = '\u212B'.encode("utf-8")
# print(newStr)
# print('\u0D05')
# print('\u25A1')
# print('\u0D00')
# print('\u0D01')

from speech import *


# # All malayalam constants
# for i in range(0x0D15, 0x0d39):
#     # even without this that number is skipped
#     if i == 0x0d29:
#         print("not available")
#     print(chr(i))

# all alphabets
def print_alphabets():
    for i in range(0x0D00, (0x0D7F + 1)):
        print(chr(i))

    speak("\u0D4C" + "\u0D15")


def show_letter():
    return "\u0d07"

# # -*- coding: utf-8 -*-
# word = "文本"
# print(word)
# for each in unicode(word,"utf-8"):
#     print(each)
