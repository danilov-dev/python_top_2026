# with open("new_file.txt", "w", encoding="utf-8") as file:
#     for i in range(3):
#         line = input("Введите текст:\n")
#         file.write(line+'\n')
# print("Файл закрыт")
#
# print("Файл открыт")
# with open("new_file.txt", "a", encoding="utf-8") as file:
#     for i in range(3):
#         line = input("Введите текст:\n")
#         file.write(line+'\n')
#
# with open("new_file.txt", "r", encoding="utf-8") as file:
#     text = file.read()
#     text_lines = text.split("\n")
#     for i in range(len(text_lines)-1,0,-1):
#         if i % 2 == 0:
#             text_lines.remove(text_lines[i])
#
# with open("new_file.txt", "w", encoding="utf-8") as file:
#     for line in text_lines:
#         file.write(line+'\n')
import json

person = {
    "name": "Alex",
    "age": 22,
    "phone": "8554658877",
    "email": ['admin@example.com', 'alex@example.com'],
    "address":{
        "city":"Msk",
        "country":"US",
        "street":"Lenina",
        "hose_number":"5"
    }
}

with open("person.json", "w") as f:
   json.dump(person, f,ensure_ascii=False, indent=4)