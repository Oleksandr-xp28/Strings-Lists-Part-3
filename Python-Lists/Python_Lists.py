import random

try:

    my_list = [] 
    
    for i in range(10):
        my_list.append(random.randint(0, 100))
        
    for value in my_list:
        print(value)
            
except Exception as e:
    print("Error:", e)

