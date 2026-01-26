# # s = "Привет мир!"
# # arr = "аеёиоуыэюя"
# # counter = 0
# # for char in s:
# #     if char in arr:
# #         counter += 1
# #
# # print(counter)
# # result = ''
# #
# # for char in s:
# #     result = char + result
# #
# # print(result)
#
# poli = "alla"
# is_poli = True
# for start in poli:
#     for end in poli[::-1]:
#         if start != end:
#             print(start, end)
#             is_poli = False
#
#
# print(is_poli)
#
# s = {'a':3, 'b':4}
# x = {'a':7, 'c':8}
#
# for key in x:
#     if key in s:
#         s[key] += x[key]
#         continue
#     s[key] = x[key]
#
# print(s)

text = "Анна Нина"
text_repl = text.split(" ")
result = {}
more_five = 0


for char in text_repl:
    if len(char) >= 5:
        more_five += 1

    if len(char) not in result.keys():
        result[len(char)] = 0

    result[len(char)] += 1

print(result)
