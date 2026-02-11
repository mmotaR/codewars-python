def positive_sum(arr):
    soma = 0 # Passo 1: variável que guarda a soma dos números positivos.
    
    for numero in arr: # Passo 2: percorre cada item da lista
        if numero > 0: # Passo 3: verificar se o número é positivo
            
            soma += numero # Passo 4: acumular apenas os positivos
    
    return soma # Passo 5: retornar o total
