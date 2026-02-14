# # num = int(input("enter a number:"))
# # if num <0: 
# #     raise ValueError("number cant be found at position")


# balance = 1000
# def add_transaction(type, amount, balance):
#     last_transactions.append(
#         {
#             "type": type,
#             "amount": amount,
#             "balance": balance,
#         }
#     )







# def deposit (user_balance):

#     amount = 0
#     while True:
#         try:
#             amount = int(input("write amount of cash"))
            
#         except:
#             print("write numebrs")
#         else:
#             break
#     user_balance += amount
#     print(f"operation complite succesfuly")
#     return user_balance







# while True:
#     print("welcome to the atm")
#     print("1 check balance")
#     print("2  ")


#     while True:
#         try:
#             num = int(input("airchiet operaciebi"))
#         except ValueError:
#             print("write only numbers")
#             num = int(input("airchiet operacia"))
#         else:
#             break
#     if operation == 1:
#         print(f"tqveni balasi {balance}")
#     elif operation == 2: 
#         new_balance = deposit(balance)
#     elif operation == 3:
#         new_balance = withdraw(balance)
#     elif operation == 4:
#         check_last_transacton()
#     elif operation == 5:
#         break
# else:
#     print("incorrect id")


# def  greet():
#     return "gamarjoba"
# def bye():
#     return "naxvamdis"



# print(higher_order(greet(), bye()))
            

# def welcome(user):
#     print("welcome", user)
# welcome('dachi')
# welcome('GOA')


# def acadmey():
#     return "Goa"


# my_numebrs = [11, 5, 7, 13, 4, 5]
# def double(x):
#     return x * 2

# print(list(map(double, my_numebrs)))


# def manual_map(func, arr):
#     result = []
#     for element in arr:
#         result.append(func(element))
#     return result



# def square(num):
#     return num ** 2

# print(manual_map(square, [1, 2, 3 ,4 ,5]))

# def get_length(x):
#     return len(x)

# print(list(map(get_length, ['luka', 'gio', 'nika', 'dato'])))


# def double(num1, num2):
#     return num1 + num2

# print (lambda num1, num2: num1 + num2)

# def is_even(num):
#     return num % 2 == 0

# print(list(filter(is_even, [1, 2, 3, 4, 5, 6, 7])))


# def manual_filter(func, iterable):
#     result = []
#     for element in iterable:
#         if func(element):
#             result.append(func(element))
#     return result



nums = [2, 7, 8, 10, 12]

def operation(x):
    return x + 5
result = map(operation, nums)

print(list(result))


def four_multipile(x):
    return x % 4 == 0
filtered = filter(four_multipile, nums)
print(list(filtered))

products ={
    "apple": [12, 5, '2028-jul-15'],
    "grapes": [15, 4, '2030-jan-20' ],
    "melon":  [20, 6, '2027-feb-1'],
    "cherry": [15, 10, '2029-jun-4'],
    "blueberry": [12, 12, '2030-may-2']

}
def no_restock(key):
    products[key][0] > 20
new_products = filter(no_restock, products)
print(list(new_products))

nums = [2, 3, 4, 5, 6, 7, 8, 9]

tripled = list(map(lambda x: x * 3,[2, 3, 4, 5, 6, 7, 8, 9]))
print(tripled)


def total (price, count):
    return price * count

print(total(1212,1212))

def greet():
    return '123'

print(greet)












        

