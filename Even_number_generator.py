#A generator which produce even numbers up to n.
def even_number_generator(n):
    for i in range(n+1):
        if i%2==0:
            print(i)
        else :
            continue
        
    return 0 


n=int(input("Enter a number upto which you want to generate a number:"))
even_number_generator(n)