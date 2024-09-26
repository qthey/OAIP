name_film = input()
name_cinema = input()
time = input()
print(f'Билет на " {name_film} " в " {name_cinema} " на {time} забронирован.')

monthly_salary = int(input('Зарплата за месяц:'))
number_of_hours_worked_on_weekends = int(input('Количество отработанных в выходных часов:'))
prize = monthly_salary * 0.01 * number_of_hours_worked_on_weekends
print('Размер премии:', prize)

sum = int(input('Введите сумму:'))
banknote_1000 = sum // 1000
sum1 = sum - (1000 * banknote_1000)
banknote_100 = sum1 // 100
sum2 = sum1 - (100 * banknote_100)
coin_10 = sum2 // 10
sum3 = sum2 - (10 * coin_10)
coin_1 = sum3 // 1
print(coin_1, '- по 1р')
print(coin_10, '- по 10р')
print(banknote_100, '- по 100р')
print(banknote_1000, '- по 1000р')

comment = input('Оцените развлекательный комплекс:')
print(comment.find('весело'))
print(comment.find('увлекательно'))
print(comment.find('развлечения'))

word = input()
print(word[(len(word)-1)//2])

feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
name1 = feedback[0:5]
name2 = feedback[8:12]
print("Назначить премию:", name1 + '/' + name2)

numb = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if numb + 3 > len(alphabet):
alphabet = alphabet * 2
print(alphabet[numb - 1:numb + 3])
else:
print(alphabet[numb - 1:numb + 3])

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.insert(0, 0)
my_list.remove(3)
del my_list[0]
slice = my_list[1:4]
reversed_list = my_list[::-1]
my_list.reverse()
two_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
my_list.clear()

empty_tuple = ()
filled_tuple = (1, 2, 3, 4, 5)
print(empty_tuple)
print(filled_tuple)

empty_set = set()
my_set = {1, 2, 3, 4, 5}
empty_set.add(6)
empty_set.add(7)
union_set = my_set.union(empty_set)
intersection_set = my_set.intersection(empty_set)
difference_set = my_set.difference(empty_set)

my_dict = {}
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict['email'] = 'john@example.com'
del my_dict['city']
my_dict['age'] = 31