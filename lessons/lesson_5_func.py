def get_min(numbers:list) -> int:
    min_num = numbers[0]
    for number in numbers:
        if number < min_num:
            min_num = number
    return min_num

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_min(my_numbers))

def get_count_numbers(text:str) -> int:
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count

print(get_count_numbers("hello world 5 ef f56fw e5 d6"))

my_array = [1, 5, 8, 10, 7]

def get_max_event_number(array:list) -> int:
    max_num = array[0]
    for number in array:
        if number > max_num:
            max_num = number
    return max_num

print(get_max_event_number(my_array))