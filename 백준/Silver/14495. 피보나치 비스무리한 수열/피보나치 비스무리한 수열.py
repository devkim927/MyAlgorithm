N = int(input())
p_list = [1, 1, 1]

for i in range(N-3):
    p_list.append(p_list[-1] + p_list[-3])

print(p_list[-1])