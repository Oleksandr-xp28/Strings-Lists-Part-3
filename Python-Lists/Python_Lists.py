import random

try:
    my_list = []
    sum = 0
    for i in range(0, 14):
        my_list.append(random.randint(0, 12))
        if my_list[i] % 2 == 0:
            print("Even", my_list[i])
            sum += my_list[i]
        else:
            print("Odd", my_list[i])
    print("List", my_list)
    print("Sum", sum)
except:
    print("Error: List is not defined")
