# 1
numbers = [2, 5, 3, 1, 4]
result = 1
for number in numbers:
    result *= number
print(result)

# 2
numbers = [2, 5, 3, 1, 4]
result = []
sum = 0
for number in numbers:
    sum += number
    result.append(sum)
print(result)

# 3
numbers = [1, 2, 2, 2, 4, 4, 5, 6, 7, 8, 8]
seen = {}
dups = []
for number in numbers:
    if number not in seen:
        seen[number] = 1
    else:
        if seen[number] == 1:
            dubs.append(number)
        seen[number] += 1

# 4
words = ['data', 'scirnce', 'machine', 'learning']
dic = {}
# -- V1 --
# count = 0
# for item in words:
#     for word in words:
#         count += 1
#     dic[item] = count
# print(dic)
# # --V2 --
# for word in words:
#     dic[word] = len(word)
# print(dic)
# --V3 --
dic = {i: len(i) for i in words}
print(dic)

# 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# grupped_numbers = []
size = 3
# for i in range(0, len(numbers), size):
#     grouped_numbers.append(numbers[i:i+size])
# print(grouped_numbers)

grupped_numbers = [numbers[i: i + size] for i in range(0, len(numbers), size)]
print(grupped_numbers)