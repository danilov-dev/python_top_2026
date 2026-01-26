# # словари
#
# person = {}
#
# car = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964,
# }
#
# # Добавление в словарь элемента
#
# person['name'] = 'Alex'
# print(person)
# person['age'] = 19
# print(person)
#
# # Получение значения по ключу
# age = person.get('age', 'error')
# print(age)
# print(person['age'])
#
# # Удаление и получение элемента по ключу
# age = person.pop('age')
# print(age)
# print(person)
#
# # вывод всех ключей или значений
# print(person.keys())
# print(person.values())
# print(person.items())
#
# persons = []
#
# for i in range(3):
#     name = input('Enter name: ')
#     age = input('Enter age: ')
#     persons.append({'name': name, 'age': age})
#
# print(persons)

# users = {
#     'Tom':{
#         'phone':'8954445862',
#         'street':'Lenina',
#     },
#     'Igor':{
#         'phone':'8115457785',
#         'street':'Titova',
#     },
#     'Elena':{
#         'phone':'9772545500',
#         'street':'Titova',
#     }
# }
#
# for user in users:
#     print(user, users.get(user))
#
# for value in users.values():
#     print(value)
#
# for user, value in users.items():
#     print(user, value)
#
# print(users['Tom']['phone'])
#
# print(users.get('Igor', {}).get('phone'))
#
# user_1 = {
#     'name': 'Tom',
#     'age': 22,
# }
# user_1_other = {
#     'street': 'Lenina',
#     'city': 'Moscow',
# }
# print(user_1)
# user_1.update(user_1_other)
# print(user_1)


users_count = 2
users = {}

for i in range(users_count):
    print(f'Input information about {i+1} user ')
    user_name = input("Enter user's name: ")
    user_age = input("Enter user's age: ")
    user_phone = input("Enter user's phone: ")
    user_address = input("Enter user's address: ")
    users[user_name] = {"age": user_age, "phone": user_phone, "address": user_address}

print(users)