import random

try:
    # Create an empty list
    my_list = [] 
    for i in range(20):
        my_list.append(random.randint(0, 15))
        
        if my_list[i] % 2 == 0:
            print("Even:", my_list[i])
except Exception as e:
    print("Error:", e)
