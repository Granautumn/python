cube_list = []
for num in range(1, 1001, 2):
    cube_list.append(num ** 3)

final_sum2 = 0
for num in cube_list:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum2 += + num

final_sum1 = 0
for num in cube_list:
    num += 17
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_sum1 += + num

print(final_sum2)
print(final_sum1)

