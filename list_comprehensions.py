def run():
    """
    # Números no divisibles entre 3
    squares = []
    for i in range(1, 101):
        if i%3 != 0:
            squares.append(i*i)

    # Muestra resultados
    print(squares)    
    
    
    # UTILIZANDO LIST COMPREHENSIONS
    squares = [i*i for i in range(1,101) if i%3 != 0]
    # [element for element in iterable if condition]
    print(squares)
    """
    
    # RETO DE LIST COMPREHENSIONS
    # Todos los mútiplos de 4 que a su vez son múltiplos de 6 y 9
    # hasta 5 dígitos
    
    reto = [i for i in range(1, 10000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(reto)
        
if __name__ == "__main__":
    run()