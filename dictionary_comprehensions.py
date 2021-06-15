import math

def run():
    
    """
    my_dict = {}
    
    for i in range (1,101):
        if i % 3 != 0:
            my_dict[i] = i**3

    print(my_dict)
    """
    my_dict = {i : i**3 for i in range(1,101) if i % 3 != 0}
    #{key:value for value in interable if condition}

    #print(my_dict)
    
    challenge = {i : math.sqrt(i) for i in range(1,1001)}
    
    print(challenge)
if __name__ == "__main__":
    run()