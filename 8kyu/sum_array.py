def sum_array(arr):
    soma = 0 # Passo 1: variável acumuladora que começa em 0
    
    # Passo 2: percorrer cada número da lista
    for numero in arr:
        
        # Passo 3: acumula a soma (inclui negativos e decimais)
        soma += numero
        
    # Passo 4: retornar o total acumulado     
    return soma 
