print('start task')

# class Mama_yyyyy:
#
#

# print('Hello world!')
# line = input()
# print(line)
#
# kartej = [1, 2, 3, 4, 5, 4]
#
# spisok = (1, (2, 3, 4), 4, 5, 6)
#
# mnojestvo = set([1, 3, 4, 5, 4])
# mnojestvo = set(spisok)
#
# print(mnojestvo)
#
# d = {'dict': 1, 'dictionary': 2}
#
# for ch in line:
#     print(ch)
#     for ch in line:
#         print(ch)


# line = "([](){([])})"
line = "(]"

line_list = []

# for ch in line:
#     line_list.append(ch)

# for ch in line_list:
#     print(ch)
#
# print('pop end', line_list.pop(len(line_list) - 1))
#
# for ch in line_list:
#     print(ch)

# print(line.index(']'))

for i in range(100):
    print(i)

for ch in line:
    if ch == '[' or ch == '(' or ch == '{':
        line_list.append(ch)
    elif ch == ']':
        temp = line_list.pop(len(line_list) - 1)
        if temp != '[':
            print('KILL ALL')
            break
    elif ch == ')':
        temp = line_list.pop(len(line_list) - 1)
        if temp != '(':
            print('KILL ALL')
            break
    elif ch == '}':
        temp = line_list.pop(len(line_list) - 1)
        if temp != '{':
            print('KILL ALL')
            break
else:
    if len(line_list) == 0:
        print('Success')
    else:
        print('KILL ALL')
# # Создаем класс Car
# class Car:
#     # создаем атрибуты класса
#     name = "c200"
#     make = "mercedez"
#     model = 2008
#
#     # создаем методы класса
#     def start(self):
#         print("Заводим двигатель")
#
#     def stop(self):
#         print("Отключаем двигатель")
#
# Car.start(Car)
# car_a = Car()
#
# car_a.start()
# car_a.stop()
