import random as rd
number_temp = rd.randint(1, 16)
number_card = [rd.randint(0, 9) for x in range(number_temp)]
# print(number_card)
print(len(number_card))
# number_card = ''.join(map(str, number_card))
# print(type(number_card))
# number_card = int(number_card)
# print(type(number_card))
new_result = []
print(number_card)

if len(number_card) <= 16 and sum(number_card) > 0:
    if len(number_card) % 2 == 0:
        result = number_card[::2]
        for item in result:
            new_result.append(item*2)
        print(new_result)
    else:
        result = number_card[1::2]
        for item in result:
            new_result.append(item*2)
        print(new_result)
for i in range(len(new_result)):
    if new_result[i] > 9:
        new_result[i] = new_result[i] - 9
print(new_result)
sum_new_result = sum(new_result)
print(sum_new_result)
if sum_new_result % 10 == 0:
    print(True)
else:
    print(False)