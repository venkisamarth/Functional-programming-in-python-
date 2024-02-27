# Adding the fucniton 
def add(a,b): 
    return a+b 
print(add(3,5))
# substraction fucntion 
def sub(a,b): 
    return a-b 
print(sub(4,6))
# MUltiplication Funcitons 
def multiply(a,b): 
   return a* b 
print(multiply(5,3))
# Division Fucntio 
def Divide(a,b): 
    return a/b
print(Divide(10,2))

#Exponetial Fucnito 
def power(base,exponent): 
    return base**exponent
print(power(2,3))
# Absulute Value Funciton 
def absolute_value(num): 
    return abs(num)
print(abs(-5))

# maximu Function 
def maximum(a,b): 
    return max(a,b)
print(maximum(10,15))

# minimum Function 
def minimum(a,b): 
    return min(a,b)
print(minimum(10,15))

# Factorial Function 
def fact(n): 
    if n==0: 
        return 1 
    else:
        return n*fact(n-1)
print(fact(0))
print(fact(1))
print(fact(5))
#Square Fucntion 
def square(num): 
    return num**2 
print(square(4))


# Intermediate Fucntion: 
# Fibonaccin  sequnce Funciton 
def fiboncaci(n): 
    if n<=1: 
        return n 
    else: 
        return fiboncaci(n-1)+fiboncaci(n-2)
print(fiboncaci(6))
# palindrome check Function: 
def is_palindrome(string): 
    return string ==string[::-1]
print(is_palindrome("randor"))
# Palindrome check fucntion 
def is_palindrome(string): 
    return string ==string[::-1]
print(is_palindrome("radero"))
print(is_palindrome("venki"))

# Prime number Check Fucntion 
def is_prime(num): 
    if num<=1: 
        return False 
    for i in range(2,int(num**0.5 )+1): 
        if num% i==0: 
            return False 
        return True
print(is_prime(17))


# List Reversal Fucntion 
def reverse_list(lst): 
    return lst[::-1]
print(reverse_list([1,2,3,4,5]))

# List Sorting Fucntio 
def flatten_list(lst): 
    return [item for sublist in lst for item in sublist]
print(flatten_list([[1,2,3],[4,5],[6,7,8]]))
# List  Filtering  fucniton 
def filter_list(lst,condition): 
    return [x for x in lst if  condition(x)]
print(filter_list([1,2,3,4,5],lambda x: x%2==0))
# Map Funciton(Requared import from functionls):
from functools import reduce 
def multiply_list(lst): 
    return  reduce(lambda x,y: x*y,lst)
print(multiply_list[1,2,3,4,5])
# Zip Function 
def zip_list(lst1,lst2): 
    return  list(zip(lst1,lst2))
print(zip_list([1,2,3],["a",'b','c']))











