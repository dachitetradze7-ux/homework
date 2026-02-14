def hello():
    return 'hello world!'
print(hello())

def greet(name):
    return "hello," + name + "!"
print(greet('dachi'))

def additional(num1,num2):
    return num1 + num2
print(additional(8,9))

def even_or_odd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(even_or_odd(9))

def average(list):
    return sum(list) / len(list)
print(average([1,2,3,4,5,6,7,8,9]))

def reversed(list):
    return list[::-1]
print(reversed([1,2,3,4,5,6,7,8,9]))

def bigger(num1,num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "they are equal"
    print(bigger(7,8))

def negative(num):
    if num < 0:
        return True
    else:
        return False
print(negative(2))

def evens(n):
    list = []
    for i in range(1,n+1):
        if i % 2 == 0:
            list.append(i)
        return list
    print(evens(18))

def vowels(word):
    count = 0
    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count += 1
    return count 
print(vowels('excellent'))
    
            





    
    


