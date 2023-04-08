import random

try:

    my_list = [] 
    
    for i in range(20):
        my_list.append(random.randint(-15, 0))
        
    for value in my_list:
        print(value)
            
except Exception as e:
    print("Error:", e)
