import random

try:
    my_list = []
    for i in range(0, 30):
        my_list.append(random.randint(0, 27))
    
    product = 1
    for i in range(0, len(my_list), 3):
        product *= my_list[i]
    print("Index:", i, "Value:", my_list[i])
    print("List:", my_list)
    print("Product multiples of 3:", product)

except Exception as e:
    print("Error:", e)
