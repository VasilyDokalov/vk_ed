#решение от chatgpt в 2 строки, вроде работает
# input_string = input("Введите строку: ")
# print("{:.2f}".format(sum(len(word) for word in input_string.split()) / max(len(input_string.split()), 1)))

input_string = input()

words = input_string.split()

total_characters = sum(len(word) for word in words)
total_words = len(words)

if total_words > 0:
    average_characters = total_characters / total_words
    formatted_average = "{:.2f}".format(average_characters)
    print(formatted_average)
else:
    print("Введена пустая строка.")
