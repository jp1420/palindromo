def words (palabra1:str, palabra2:str):
    encontradas = []
    noencontradas = []
    for i in palabra1:
        if i in palabra2:
            encontradas.append(i)
        else:
            noencontradas.append(i)
    print(f'Las letras que se repiten son {set(encontradas)}')
    '''conjuntos(1,2,2,2,2,3) se deja editar pero no repetir y se manipula por 'set' pocas palabras
    set esta poniendo las letras pero no las repite lo cual si pongo inteligente y estupido no se 
    va a repetir 3 veces la e en inteligente con el set'''

    for x in palabra2:
        if x not in palabra1:
            noencontradas.append(x)
    print(f'Las letras que no se repiten son {set(noencontradas)}')
    
''' el not in es para si no esta, en pocas palabras en la primera funcion estaba poniendo las que se
repetian, y con la segunda funcion en el for x, pongo not in para decirle practicamente las que 
las ponga en la otra lista, las cuales no se repiten'''
       

palabra1 = input('ingrese la primera palabra:')
palabra2 = input('ingrese la segunda palabra:')

words(palabra1, palabra2)

    

