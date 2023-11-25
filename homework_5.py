a = int(input())
b = float(input())
c = int(input())

formatted_a = "+" + str(a).zfill(9)
print(formatted_a)

formatted_b = "######" + "{:.2f}".format(b)
print(formatted_b)

binary_representation = format(c, '016b')
formatted_c = '_'.join([binary_representation[i:i+4] for i in range(0, len(binary_representation), 4)])
print(c)
