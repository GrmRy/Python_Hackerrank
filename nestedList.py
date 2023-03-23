answer = ""
result = []
ans1 = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name, score])
sorted_list = sorted(result, key=lambda x: x[1])
ans1 = (item[1] for item in sorted_list)
sorted_list2 = list(set(ans1))
sorted_list2.sort()
sorted_list = list(filter(lambda x: x[1] == sorted_list2[1], sorted_list))
result1 = sorted(sorted_list, key=lambda x: x[0])
answer  =  "\n".join(item[0] for item in result1)
print(answer)
