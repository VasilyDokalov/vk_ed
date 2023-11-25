# a = int(input())
# b = int(input())
# c = bool()
#
# while i := input():
#     i = int(i)
#     if a <= i <= b:
#         c = True
#         continue
#     elif i < a or i > b:
#         c = False
#         continue
# print(c)
a = int(input())
b = int(input())
c = True

while i := input():
    i = int(i)
    if i < a or i > b:
        c = False
        break
print(c)
