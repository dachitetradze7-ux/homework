# def add_arguments(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total   
# print (add_arguments(12, 13, 23, 46, 78 ,89))
# print("dachi", "luka", "nika", sep= " ! ") 



# vegetables = ("pumpkin", "cabbage", "beetroot")
# product1, *rest = vegetables

# print(rest)
# print(product1)


# def greeting(visitor,  *guests, special, **kwargs):
#     print("welcome " + visitor)
#     for guest in guests:
#         print("hello " + guest)
#     print("salami " + special)
#     print(kwargs)
#     for key in kwargs:
#         print(f"hello {key} {kwargs[key]}")

    
# greeting("irakli", "zurab", "nika", "dachi", special = "zurab", celebrity = "zaza", influ = "davit")
         
# # args = განუსაზღვრელი არგუმენტი რომელიც tuples გვაძლევს    
# 

# scope = ხედვის არეალი

# def any():
#     global z
#     z = 13400
#     def a():
#         print(z)
#         x = 5
# any()
# print(z)

# def format_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return "sum: " +str(result)
#     return wrapper

