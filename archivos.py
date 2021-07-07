def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as data:
        for line in data:
            numbers.append(int(line))
            
    print(numbers)
        
def write():
    names = ["Facundo", "Miguel", "Pepe", "Christian", "Fernández"]
    with open("./files/numbers.txt", "a") as data:
        for name in names:
            data.write(name)
            data.write("\n")
    
    # whith open("/directory", "mode", encoding="utf-8") as f:
    # Modes
        # a = Append
        # r = Read
        # w = Write
    # Filename = f (Usualy this way)
    
def run():
    #read()
    write()

if __name__ == "__main__":
    run()