#name_film = input()
#name_cinema = input()
#time = input()
#print('Билеты на "', name_film, '"', 'в', '"', name_cinema, '"', 'на', time, 'забронирован.')

monthly_salary = int(input('Зарплата за месяц:'))
number_of_hours_worked_on_weekends = int(input('Количество отработанных в выходных часов:'))
prize = monthly_salary * 0.01 * number_of_hours_worked_on_weekends
print('Размер премии:', prize)