word = input()
# good_letters = "ao"
# bad_letters = "ie"
# for letter in good_letters:
#     if letter in word:
#         if letter not in bad_letters:
#             print(True)
#         else:
#             print(False)
if ("a" in word or "o" in word) and "i" not in word and "e" not in word:
    print(True)
else:
    print(False)
