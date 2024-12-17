import random


#Функция создания случайного списка из чисел
def generation_list():
    count = random.randint(1, 20)
    random_list = []
    for _ in range(count):
        random_list.append(random.randint(-100, 100))
    return random_list


#Функция сложения двух списков
def summa_lists(list_1, list_2):
    if len(list_1) > len(list_2):
        result = list_1
        for index in range(len(list_2)):
            result[index] += list_2[index]
    else:
        result = list_2
        for index in range(len(list_1)):
            result[index] += list_1[index]
    return result


#Основное тело программы
first_list = generation_list()
second_list = generation_list()

print("Первый список: ", first_list)
print("Второй список: ", second_list)
print("Сумма списков: ", summa_lists(first_list, second_list))