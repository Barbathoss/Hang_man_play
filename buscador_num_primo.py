def run(valor):   
    for i in range(2,valor+1):     # Ciclo incrementa i : Dividendo 
        for j in range(2,valor+1): # Ciclo incrementa j; Divisor             
            if j >= i:                                                          # Si el Divisor llega a ser mayor o igual que el dividendo.
                print(i, '   Es numero primo ' )                                # El numero es primo y se interrumpe el ciclo. 
                break                            
            elif i>j and i%j==0 and j>1:                                        # Si el dividendo es mayor que el divisor, el divisor es mayor que 1 y la division es exacta.
                break                                                           # El numero no es primo y se interrumpe el ciclo.
                
              
if __name__ == '__main__':
    print('Buscador de numeros primos')
    n = int(input('Por favor ingrese el rango maximo para la busqueda: '))
    run(n)