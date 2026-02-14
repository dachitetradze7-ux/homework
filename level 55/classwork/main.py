# # method - უბრალო კლასის ფუნქცია რომელიც აუიცლელბად ღებულობს პარამეტრად "self"-ს რაც გულსხმიბს იმ ობიექტს რომლებსაც მომავალში შევქმნთ კონკრეტული კლასით, ეს მეთოდი კი მხოლოდ ამ ინსტანციებზე (კონკრეტულ მაგალითზე) იქნება გამოძახებდი და მათზე შეასრულებს დავალებებს

# # classmethod - ამ მეთოდის (ფუნქციის) დეკორაციას ვახდენთ @classdecorator-ით, ასევე კლასის მეთოდი აუციელბლად ღებულობს პარამეტრად "cls" რაც წაროადგენს თვითნ იმ კლასს რომელშიც ვქმნთ ამ მეთოდს, კლასის მეთოდს შეეძლება მიწვდეს კლასის ზოგად ცვლადებს და კლასისთვის დამახისათებელი ზოგადი ატრიბუტი შეცვალოს

# # staticmethod - იქმნება @staticdecorator დეკორატორ ფუნქციით და მკაცრად არ მოთხევა კონკრეტული პარამეტრების მიღება, მას ვიყენებთ მაშინ როცა ის კავშირშია კლასსთან და მის ობიექტან მაგრამ ისე რომ არ გვჭირდება რომელიე ობიექტის ან კლასის ატრიბუტის გამოყენება

# # დაფარული კუთვნილებები
# # protected - დაცული კუთვნილება რომელიც ხელმისწავდომია კლასის გარეთაც, მაგრამ ამ დროს ვიჩენთ სიფრთხილეს
# # private - კონფიდენციალური კუთვნილება რომელიც კლასის მეთოდის გარეთ ფიზიკურად არაა ხელმისწავდომი, მისი გამოყენება შესაძლებელია მხოლოდ კლასის შიგნით 

# class Group:
#     channels = ["cw", "hw", "stage", "voice"]
#     def __init__(self, students, mentor, assistant):
#         self.students = students
#         self._mentor = mentor # protected property
#         self.__assistant = assistant # private
    
#     # getter
#     def get_assistant(self):
#         return self.__assistant

#     def change_asssitant(self, new_asssitant):
#         self.__assistant = new_asssitant

#     @classmethod
#     def get_channels(cls):
#         print (cls.channels)
#         print(Group.__assistant)
  



# group_88 = Group(14, "Luka", "Giorgi")

# # არასწორი გზა
# group_88.__assistant = "Ilia"
# # სწორი გზა
# # group_88.change_mentor("Ilia")


# group_89 = Group(10, "Nika", "Zaza")

# # print(group_88.students)
# # print(group_88.mentor)
# # print(group_88.get_assistant())


# # print(group_88.__assistant)

# # name mangling
# print(group_88._Group__assistant)

number = 50
if number > 100:
    print(False)








