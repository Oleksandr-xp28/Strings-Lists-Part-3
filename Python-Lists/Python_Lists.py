import random

try:
    # Create an empty list
    my_list = [] 
    for i in range(25):
        my_list.append(random.randint(0, 50))
    print("The list is:", my_list)
    print("The length of the list is:", len(my_list))
    print("The maximum value in the list is:", max(my_list))
    print("The minimum value in the list is:", min(my_list))
    print("The sum of the list is:", sum(my_list))
    print("The average of the list is:", sum(my_list) / len(my_list))
    print("The first element in the list is:", my_list[0])
    print("The last element in the list is:", my_list[-1])
    print("The first 5 elements in the list are:", my_list[0:5])
    print("The last 5 elements in the list are:", my_list[-5:])
    print("The list in reverse order is:", my_list[::-1])
    print("The list in sorted order is:", sorted(my_list))
    print("The list in reverse sorted order is:", sorted(my_list, reverse=True))
    print("The list in sorted order is:", my_list.sort())

except Exception as e:
    print("Error:", e)
