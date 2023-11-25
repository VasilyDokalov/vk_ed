input_string = input()

modified_string = input_string.lower().replace('!', '').replace('%', '').replace('#', '').replace('@', '')

num_replacements = len(input_string) - len(modified_string)

print(num_replacements)
print(modified_string)