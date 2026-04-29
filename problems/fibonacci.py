def main():
    n = int(input("Give me n: "))
    print(fibonacci(n))



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        n_1 = 1
        n_0 = 0
        
        for _ in range(1,n):
            output = n_1 + n_0
            n_0 = n_1
            n_1 = output
   

        return output
    
main()