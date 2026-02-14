# new_menu = []

# dish1="pizza"
# dish2="pasta"
# dish3="salad"

# def add_to_menu(menu,dish):
#     menu.append(dish)

# add_to_menu(new_menu,dish1)
# print(new_menu)


# add_to_menu(new_menu,dish2)
# print(new_menu)


# add_to_menu(new_menu,dish3)
# print(new_menu)

# cart = []

# def add_to_cart(cart):
#     product = input()
#     cart.append(product)

# add_to_cart(cart)
# print(cart)

# cart = []
# def add_to_cart(cart):
#   product = input()
#   product.append(cart)
# print("score"<5 or "score">10)

# def my_function(score):
#   if score >= 70:
#     return True

# print(my_function(score))

# books = ['1984', 'war and peace', 'the great gatsby']
# book = 'animal farm'

# def book_in_library(books,book):
#     return book in books
# print(book_in_library(books,book))

# library= ['book', 'desk', 'dog']
# print(len(library))

# products = ['pen', 'pencil', 'ruler']
# print(len(products))

# price = [33,59,42,43,53]
# total=sum(price)
# print("total price:", total)


# number_of_products = len(price)
# print("count:", number_of_products)


# avg_price = total/number_of_products
# print("average price:", avg_price
# print(max(price))
# print(min(price))

# ages = [33, 14, 30, 49]
# sorted_ages = sorted(ages)
# print(sorted_ages)

# prices = [503.9, 199.9, 254.5, 39.9]
# srt_prices = sorted(prices)
# print(srt_prices[1])

# palyers = ["zoe", "liam", "emma", "noah"]
# srt_players = (sorted(palyers))
# print(srt_players)

# message = "Welcome"
# def greeting(text):
#   print(text)

# string მეთოდები: split, join, reolace, strip

# split: გამოიყენება string_ზე string.split(გაყოფის სტრინგი)
# ეს მეთოდი ერთ დიდ სტრინგს დაშლის ცალ-ცალკე სტრინგებად და შეინახავს და შეინახავს სიაში

# join: string.join

sentence = "the dog has climbed over the tree"

words = sentence.split(" ")
print(words)

words = ["the", "dog", "has", "climbed", "over", "the", "tree"]
sentence = " ".join(words)


print(sentence)


word = "bla bla bla"
new_word= word.replace("la", "ja")
print(new_word)

word = "magic spell mana mana magic spell magic"
new_word = word.replace("mana", "dachi")
print(new_word)

any_string = "!!!!! GOA  ###### !!!!!"
trained_string = any_string.strip("!")
print(any_string)
print(trained_string)

