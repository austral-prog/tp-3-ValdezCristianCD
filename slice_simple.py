def slice_simple():
    texto = "awesome"
    
    print(texto[0:3])
    print( texto[ int(len(texto)/2-1) : int(len(texto)/2+2) ] )
    print(texto[0:4] + texto[-3:])

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
