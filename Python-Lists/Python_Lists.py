import random


my_list = [random.randint(-10, 10) for i in range(20)]


first_positive_index = 0
while my_list[first_positive_index] <= 0:
    first_positive_index += 1


last_positive_index = len(my_list) - 1
while my_list[last_positive_index] <= 0:
    last_positive_index -= 1


sum_between = 0
for i in range(first_positive_index + 1, last_positive_index):
    sum_between += my_list[i]

print("List:", my_list)
print("Sum of elements between the first and last positive element:", sum_between)

