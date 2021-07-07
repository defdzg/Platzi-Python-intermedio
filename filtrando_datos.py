from data_to_filter import DATA

def run():
    """
    ########### CLASE ###########
    
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == 'python']

    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == 'Platzi']
    
    # Práctica de High Order Functions con Lambda Functions
    
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70},DATA)) 
                                            # PIPE: Unir a un diccionario con otro nuevo
                                            
    for worker in old_people:
        pass
        #print(worker)
        
    """
    
    ###########  RETO ###########
    
    all_python_devs = list(filter(lambda dev: dev["language"] == "python", DATA))
    all_python_devs = list(map(lambda dev: dev["name"], all_python_devs))
    
    for dev in all_python_devs:
        print(f'{dev} knows Python.') 

    print("-"*20)

    
    all_Platzi_worker = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_Platzi_worker = list(map(lambda worker: worker["name"], all_Platzi_worker))
    

    for worker in all_Platzi_worker:
        print(f'{worker} works at Platzi.') 

    print("-"*20)

    old_people = [worker["name"] for worker in DATA if worker["age"] > 70]
    for person in old_people:
        print(f'{person} has more than 70 years old.')
    
    print("-"*20)
    
    adutls = [worker["name"] for worker in DATA if worker["age"] >17]
    for person in adutls:
        print(f'{person} is an adult.')
        
        
# ENTRY POINT

if __name__ == '__main__':
    run()