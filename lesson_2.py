#
# # Срезы
# cars = ['bmw', 'honda', 'toyota', 'lada']
#
# print(cars)
# print(cars[:2])
# print(cars[-2:])
#
# # Инверсия списка срезами
# print(cars[::-1])
#
# for car in cars:
#     if len(car) > 3:
#         print(f'В слове {car} - {len(cars)} символов')


# name = input('Введите свое имя: ')
# if name:
#     print(f'Привет {name}')

N = 3
my_list = []
END_WORD = 'end'

while True:
    word = input('Enter a word: ')
    if word:
        if word.lower() == END_WORD:
            print('End word entered')
            break

        if word[-1] == '!':
            my_list.append(word)

print(my_list)
