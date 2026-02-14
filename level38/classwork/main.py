#dictionary
#key/value - წყვილების ერთობლიობა
#dictionary keys - brand, model, year, price
#dictionary values - hyundai, jeep, 2015, 4000
#dictioanry - keys cant be mutable
# my_car = {}
# print(type(my_car))

# my_car = {
#     "brand": "hyundai",
#     "model": "jeep",
#     "year":  2015,
#     "price": 4000,
#     "sold":  True
# }
# for item in my_car.items():
#     print(item)


# for key, value in my_car.items():
#     print(f"key: {key}, value: {value}")
#     print(my_car)
# for key, value in my_car.items():
#     print(item)

# # my_car.pop("sold")
# # print(my_car)

# # print(my_car.keys())
# # print(my_car.values())
# # print(my_car.items())

# new_car = my_car.copy()
# print(new_car)
# print(id(my_car))
# print(id(new_car))


# pc_system = {
#     "gpu": "1660GTX",
#     "cpu":  "i5 10400f",
#     "hdd":  "256gb",
#     "ssd":  "512"
# }

# print(pc_system["gpu"])
# print(pc_system["cpu"])
# print(pc_system["hdd"])
# print(pc_system["ssd"])


# pc_system.pop("hdd")
# pc_system.clear()
# # pc_system.update {
# #     "gpu": "nvidia"
# # }
# pc_system_higher = pc_system
# pc_system_higher = pc_system.copy()
# pc_system["hdd"] = "1tb"
# print(id(pc_system))
# print(id(pc_system_higher))
# print(pc_system_higher.items())


# numbers = [54, 25, 23, 26, 63, 45, 15, 37]
# evens = [num + 1 for num in numbers if num % 2 == 0]

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
# print(evens)


# new_evens = [i + 1 for i in numbers if i % 2 == 0]
# print(new_evens)

# lucky_numbers = [n * n + 3 for n in range(1, 21) if n % 4 == 0]
# print(lucky_numbers)

# special_list = [a for a in range(1, 20) if a % 2 == 0]
# print(special_list)


sentence = "we are learning dictionries & list comperhensions"
char = "###"
my_data = [char + "###" for char in sentence]
print(my_data)

