def calc_fibonacci(n): 
    if n<0:
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return calc_fibonacci(n-1)+calc_fibonacci(n-2)

def calc_fibonacciOptimized(n, ant=0, sig=1): 
    if n<0:
        print("Incorrect input")
    elif n==0: 
        return ant
    return calc_fibonacciOptimized(n-1, sig, ant+sig)


num = int(input("Ingresa cuantos numeros de Fibonacci deseas encontrar: ")) 
  
if num<=0:
    print("Por favor ingresa un entero positivo")
else:
    for i in range(num):
        print(calc_fibonacciOptimized(i), end=" ")
