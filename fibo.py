def sequencia(x):
    #função que define a sequencia Fibonacci
    a, b = 0, 1
    seqFibo = []
    for _ in range(x):
        seqFibo.append(a)
        a, b = b, a + b
    return seqFibo

def main():
   
    x = 10  # Número de termos da sequência de Fibonacci
    seqFibo = sequencia(x) 

    while True:
        a = int(input('Digite um número: '))  # Entrada do número
        
        # Verificação se o número informado pertence à sequência de Fibonacci
        if a in seqFibo:  
            print('Parabéns! O número informado pertence à sequência!')
            break
        else:
            print('O número não pertence à sequência, tente novamente!')

if __name__ == "__main__":
    main()