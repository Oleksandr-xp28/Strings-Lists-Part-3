import random

try:
    my_list = []
    sum = 0
    for i in range(0, 14):
        my_list.append(random.randint(-12, 12))
        if my_list[i] < 0:
            sum += my_list[i]
        else:
            my_list[i] = 0
    print("List", my_list)
    print("Sum", sum)
except:
    print("Error: List is not defined")
