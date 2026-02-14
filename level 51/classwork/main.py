# nums = [2, 7, 8, 10, 12]

# def operation(x):
#     return x + 5
# result = map(operation, nums)

# print(list(result))


# def four_multipile(x):
#     return x % 4 == 0
# filtered = filter(four_multipile, nums)
# print(list(filtered))

# products ={
#     "apple": [12, 5, '2028-jul-15'],
#     "grapes": [15, 4, '2030-jan-20' ],
#     "melon":  [20, 6, '2027-feb-1'],
#     "cherry": [15, 10, '2029-jun-4'],
#     "blueberry": [12, 12, '2030-may-2']

# }
# def no_restock(key):
#     products[key][0] > 20
# new_products = filter(no_restock, products)
# print(list(new_products))

# nums = [2, 3, 4, 5, 6, 7, 8, 9]

# tripled = list(map(lambda x: x * 3,[2, 3, 4, 5, 6, 7, 8, 9]))
# print(tripled)


# def total (price, count):
#     return price * count

# print(total(1212,1212))

# def greet():
#     return '123'

# print(greet)

# info = products.copy()
# info['cherry'][0] = 10
# print(products)

# any = lambda name: "#" + name
# print(type(any))

# def mult(n):
#     return lambda a: a * n
# tripler = mult(3)
# doubler = tripler(2)
# print(doubler)

# lambda_func = mult(25)

# print(lambda_func(2))
# print(lambda_func(4))


# print(doubler(2))
# print(tripler(5)) 

#callback - 
# def x():
#     return 1

# def eveulate(func):
#     return func()

# eveulate(x)



def func1():
    print ("hello function from GOA!")
    return 5

def func2(func):
    def wrapper():
        print("--------start------")
        x = func()
        print("-----end-----")
        return x
    return wrapper

f = func2(func1)
print(f())
    
    
     
     
    








