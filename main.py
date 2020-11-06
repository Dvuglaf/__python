# 5 вариант
import re


def find_values(user_dict, maximum):
    return_list = []
    value = 0.
    if not maximum:
        value = float('inf')
    for key in user_dict:
        if not maximum:
            if user_dict[key][0] < value:
                value = user_dict[key][0]
                continue
        elif user_dict[key][0] > value:
            value = user_dict[key][0]
    for key in user_dict:
        if user_dict[key][0] == value:
            return_list.append(key)
    return return_list


def find_sum(user_dict, maximum):
    return_list = []
    value = 0.
    if not maximum:
        value = float('inf')
    for key in user_dict:
        if not maximum:
            if user_dict[key][1] + user_dict[key][2] + user_dict[key][3] < value:
                value = user_dict[key][1] + user_dict[key][2] + user_dict[key][3]
                continue
        elif user_dict[key][1] + user_dict[key][2] + user_dict[key][3] > value:
            value = user_dict[key][1] + user_dict[key][2] + user_dict[key][3]
    for key in user_dict:
        if user_dict[key][1] + user_dict[key][2] + user_dict[key][3] == value:
            return_list.append(key)
    return return_list


regex = r'(?<=<td>)[^><]+(?=</td>)'
with open("html.txt", "r", encoding="utf8") as file:
    text = file.read()

search = re.findall(regex, text)
dictionary = {}
for i in range(0, len(search), 5):
    dictionary.update({
        search[i]: [float(search[i + 1]), float(search[i + 2]), float(search[i + 3]), float(search[i + 4])]
    })

string = "Суммарное количество неповторяющихся записей в таблицах: " + str(len(dictionary)) + "\n"

temp = find_values(dictionary, True)
string += "\nМаксимальная энергетическая ценность (" + str(dictionary.get(temp[0])[0]) + " ккал):\n"
for i in temp:
    string += i + "\n"

temp = find_values(dictionary, False)
string += "\nМинимальная энергетическая ценность (" + str(dictionary.get(temp[0])[0]) + " ккал):\n"
for i in temp:
    string += i + "\n"

temp = find_sum(dictionary, True)
string += "\nМаксимальное суммарное содержание белков, жиров и углеводов (" + str(sum(dictionary.get(temp[0]),
                                                                                      -dictionary.get(temp[0])[0])) + \
          " грамм):\n"
for i in temp:
    string += i + "\n"

temp = find_sum(dictionary, False)
string += "\nМинимальное суммарное содержание белков, жиров и углеводов (" + str(sum(dictionary.get(temp[0]),
                                                                                     -dictionary.get(temp[0])[0])) + \
          " грамм):\n"
for i in temp:
    string += i + "\n"

with open("result.txt", "w", encoding="utf8") as file:
    file.write(string)
