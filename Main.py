import requests
from bs4 import BeautifulSoup

"""Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)

Какова сложность вашего алгоритма?

def task(array):
  pass

print(task("111111111111111111111111100000000"))
# >> OUT: 25...
============================
"""

def task1(array):
    answer = array.index("10") + 1
    return answer

"""Это наверное не то что вы от меня ждали :-)"""

def task1v2(array):
    item = "10"
    
    low = 0
    high = len(array)
    if str(array[0:2]) == "10":
        return 2
    else:
        while low <= high:
            mid = round((low + high)/2)
            guess = str(array[mid - 1:mid + 1])
            if guess == item:
                return mid
            elif guess == "11":
                low = mid
            else:
                high = mid
    return None



"""Task 2:
В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (Категория:Животные по алфавиту) и вывести количество животных на каждую букву алфавита. Результат должен получиться в следующем виде:
 А: 642
Б: 412
В:....
"""
def Task2():

    alp = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"

    answer = {'А' : 0, 'Б' : 0, 'В' : 0, 'Г' : 0, 'Д' : 0, 'Е' : 0, 'Ё' : 0 , 'Ж' :0, 'З' : 0, 'И' : 0, 'Й' : 0, 'К' : 0 , 'Л' : 0, 'М' : 0, 'Н' : 0, 'О' : 0, 'П' : 0, 'Р' : 0, 'С' : 0, 'Т' : 0, 'У' : 0, 'Ф' : 0, 'Х' : 0, 'Ц' : 0, 'Ч' : 0, 'Ш' : 0, 'Щ' : 0, 'Э' : 0, 'Ю' :0, 'Я': 0, 'A' : 0,  'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0, 'H' : 0, 'I' : 0, 'J' : 0, 'K' : 0, 'L' : 0, 'M' : 0, 'N' : 0, 'O' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0, 'T' : 0, 'U' : 0, 'V' : 0, 'W' : 0, 'X' : 0, 'Y' : 0, 'Z' : 0, }
    latter = 'Zyzzyx chilensis'

    URL = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"
    names = []

    HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'
        , 'accept': '*/*'}
    r = requests.get(URL, headers = HEADERS, )
    soup = BeautifulSoup(r.text, 'html.parser')
    category = soup.find("div", class_="mw-content-ltr",)
    items= category.select(' li > a')
    for item in items:
        names.append(item.text)

    while names[-1] != latter:

        URL = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту&pagefrom=" + names[-1]
        r = requests.get(URL, headers = HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        category = soup.find("div", class_="mw-content-ltr", )
        items = category.select(' li > a')
        for item in items:
            names.append(item.text)

    set(names)

    for name in names:
        answer[str(name[0])] += 1

    for i in alp:
        print("{0}: {1}".format(i, answer.get(i)))

"""Task 3:
Мы сохраняем время присутствия каждого пользователя на уроке  виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах): — lesson – начало и конец урока 
— pupil – интервалы присутствия ученика 
— tutor – интервалы присутствия учителя 
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах). 
Будет плюсом: Написать WEB API с единственным endpoint’ом для вызова этой функции.
"""
def appearance(intervals):

    lesson = intervals.get("lesson")
    pupil = intervals.get("pupil")
    tutor = intervals.get("tutor")
    time = 0
    tutor_in_lesson = []
    pupil_in_tutor = []
    #ПРОВЕРИТЬ ВСЕ ВРЕМЯ УЧИТЕЛЯ В КЛАССЕ
    for i in range(0,len(tutor),2):
        if tutor[i] < lesson[0] and tutor[i + 1] < lesson[1]:
            tutor_in_lesson.append([lesson[0],tutor[i + 1]])

        elif tutor[i] < lesson[0] and tutor[i + 1] >= lesson[1]:
            tutor_in_lesson.append([lesson[0],lesson[1] ])

        elif tutor[i] >= lesson[0] and tutor[i + 1] >= lesson[1]:
            tutor_in_lesson.append([tutor[i],lesson[1]])

        elif tutor[i] >= lesson[0] and tutor[i + 1] < lesson[1]:
            tutor_in_lesson.append([tutor[i],tutor[i + 1]])

    #ПРОВЕРИТЬ ВСЕ ВРЕМЯ УЧЕНИКА ВО ВРЕМЯ УЧИТЕЛЯ В КЛАССЕ
    for j in range(len(tutor_in_lesson)):
        for i in range(0, len(pupil), 2):
            if pupil[i + 1] > tutor_in_lesson[j][0]:
                if pupil[i] <  tutor_in_lesson[j][0] and pupil[i + 1] < tutor_in_lesson[j][1]:
                    pupil_in_tutor.append([tutor_in_lesson[j][0], pupil[i + 1]])

                elif pupil[i] <  tutor_in_lesson[j][0] and pupil[i + 1] >= tutor_in_lesson[j][1]:
                    pupil_in_tutor.append([tutor_in_lesson[j][0], tutor_in_lesson[j][1]])

                elif pupil[i] >= tutor_in_lesson[j][0] and pupil[i + 1] >= tutor_in_lesson[j][1]:
                    pupil_in_tutor.append([pupil[i], tutor_in_lesson[j][1]])

                elif pupil[i] >= tutor_in_lesson[j][0] and pupil[i + 1] < tutor_in_lesson[j][1]:
                    pupil_in_tutor.append([pupil[i], pupil[i + 1]])

    for i in pupil_in_tutor:
        time = time + abs(i[1] - i[0])
    return time



#========================================================================================================

intervals = {
  'lesson': [1594663200, 1594666800],
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
}
print(task1("111111111111111111111111100000000"))
print(task1v2("111111111111111111111111100000000"))
Task2()
print(appearance({
  'lesson': [1594663200, 1594666800],
  'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
  'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
}))
