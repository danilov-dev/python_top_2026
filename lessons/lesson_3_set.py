# множества - set

set_of_cars = set()

set_of_cars.add('bmw')
set_of_cars.add('lada')
set_of_cars.add('audi')
print(set_of_cars)
# set_of_cars.remove('lada')
# set_of_cars.discard('lada11')
print(set_of_cars)

for car in set_of_cars:
    print(car)

set_of_cars2 = {'audi','uaz','mazda'}

# обьединение множеств
result_set_of_cars = set_of_cars.union(set_of_cars2)
print(result_set_of_cars)
print(set_of_cars | set_of_cars2)

# пересечение множеств
result_set_of_cars = set_of_cars.intersection(set_of_cars2)
print(result_set_of_cars)
print(set_of_cars & set_of_cars2)

# разность множеств
result_set_of_cars = set_of_cars.difference(set_of_cars2)
print(result_set_of_cars)
print(set_of_cars - set_of_cars2)

# симметричная разность множеств
result_set_of_cars = set_of_cars.symmetric_difference(set_of_cars2)
print(result_set_of_cars)
print(set_of_cars ^ set_of_cars2)

#issubset
users = {'Masha', 'Dasha', 'Sasha', 'Lena'}
super_users = {'Sasha', 'Lena'}

print(users.issuperset(super_users))
print(super_users.issuperset(users))

persons = frozenset({'Masha', 'Dasha', 'Sasha', 'Lena'})


