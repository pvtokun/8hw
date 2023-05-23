import datetime

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = datetime.datetime.now().date()
    
    # Визначаємо перший день тижня (понеділок)
    start_of_week = current_date - datetime.timedelta(days=current_date.weekday())
    
    # Створюємо словник для зберігання іменинників по днях
    birthdays_per_day = {}
    
    # Перебираємо користувачів
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        
        # Визначаємо день народження у поточному тижні
        birthday_in_week = start_of_week + datetime.timedelta(days=(birthday.weekday() - start_of_week.weekday()) % 7)
        
        # Додаємо користувача до відповідного дня в словнику
        if birthday_in_week in birthdays_per_day:
            birthdays_per_day[birthday_in_week].append(name)
        else:
            birthdays_per_day[birthday_in_week] = [name]
    
    # Виводимо іменинників по днях
    for day in sorted(birthdays_per_day.keys()):
        day_name = day.strftime('%A')
        birthday_names = ', '.join(birthdays_per_day[day])
        print(f"{day_name}: {birthday_names}")

# Приклад використання

users = [
    {'name': 'Bill', 'birthday': datetime.datetime(2000, 3, 15)},
    {'name': 'Jill', 'birthday': datetime.datetime(1995, 8, 20)},
    {'name': 'Kim', 'birthday': datetime.datetime(1987, 4, 10)},
    {'name': 'Jan', 'birthday': datetime.datetime(1992, 10, 30)},
    {'name': 'Sam', 'birthday': datetime.datetime(2002, 6, 5)},
    {'name': 'Nazar', 'birthday': datetime.datetime(2005, 5, 15)},
]

get_birthdays_per_week(users)