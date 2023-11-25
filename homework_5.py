a = int(input())
b = float(input())
c = int(input())

print(f"{a:0=+10}")

# if b >= 0:
#     print(f"{round(b, 2):#>10}")
# else:
#     print(f"{round(b, 2):#>9}")

if b >= 0:
    print(f"{b:#>10.2f}")
else:
    print(f"{b:#>+10.2f}")

res_current = format(c, '016b')[::-1]
formatted_res = '_'.join([res_current[i:i+4] for i in range(0, len(res_current), 4)])[::-1]
print(formatted_res)