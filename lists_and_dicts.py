def main():
    
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {"fistname": "Daniel", "lastname": "Fernández"}
    
    super_list = [
        {"fistname": "Daniel", "lastname": "Fernández"},
        {"fistname": "Miguel", "lastname": "Osteguín"},
        {"fistname": "Marcela", "lastname": "García"},
        {"fistname": "Ivanna", "lastname": "Osteguín"},
    ]
    
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 53.12]
    }
    
    # Shows in CLI list contained in the Super Dictionary
    
    for key, value in super_dict.items():
        print(key, "-", value)

    # Shows in CLI Dictionary values from existing keys
    for item in super_list:
        print(item["fistname"], item["lastname"])
        
if __name__ == "__main__":
    main()