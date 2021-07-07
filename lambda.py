# Funciones anónimas (Lambda Functions)
# No tienen un identificador (nombre)

    # lambda argumentos: expresión
    # Sólamente pueden tener una expresión
    
palindorme = lambda string: string == string[::-1]

# No es necesario usar la palabra return
print(palindorme('ana'))