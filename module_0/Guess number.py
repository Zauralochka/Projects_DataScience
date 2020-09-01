#!/usr/bin/env python
# coding: utf-8

# #  Программа угадывания числа от 1 до 100
# 

# In[16]:


import numpy as np                   # импортируем библиотеку numpy
count = 0                            # обнуляем счетчик попыток
number = np.random.randint(1,100)    # генерируем случайное число от 1 до 100

def game_core_v4(number):
    
    '''Функция нахождения числа от 1 до 100. Сравниваем загаданное число 
       с серединой диапазона чисел, постепенно сокращая диапазон поиска вдвое.
       Функция принимает загаданное число и возвращает число попыток'''
    
    count = 1
    begin_predict_range = 1  # задаем начало диапазона чисел
    end_predict_range = 100  # задаем конец диапазона чисел
    predict = (end_predict_range + begin_predict_range)// 2 # определяем середину диапазона чисел
    while number != predict: # выполняем цикл до тех пор пока предополагаемое число не равно загаданному числу
        #print(range(begin_predict_range, end_predict_range), predict) вывод на экран при тестировании
        count+=1 # считаем попытки
        if number > predict: # при условии, что загаданное число больше предполагаемого
            if (end_predict_range - begin_predict_range) > 4:
                begin_predict_range = predict + 1 #начало диапазона смещается вправо на одно число от середины 
                predict =(end_predict_range + begin_predict_range)// 2 
            else:
                begin_predict_range = predict # при диапазоне чисел <=4 начало смещается в середину
                predict = begin_predict_range + 1 # предпалагаемое число увеличивается на 1 от начала
        elif number < predict: # при условии, что загаданное число меньше предполагаемого
            if (end_predict_range - begin_predict_range) > 4: 
                end_predict_range = predict - 1  #конец диапазона смещается влево на одно число от середины
                predict =(end_predict_range + begin_predict_range)// 2
            else:
                end_predict_range = predict  #в случае диапазона чисел <= 4
                predict = end_predict_range - 1  # предполагаемое число уменьшается на 1 от конца
        
    else:
        print("Вы угадали, загаданное число равно {}, число попыток равно {}".format(number, count))
    return(count) # выход из цикла, если число угадано

def score_game(game_core):
    
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,100, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[10]:


game_core_v4(number)


# In[17]:


score_game(game_core_v4)

