from datetime import datetime
import random

if __name__ == '__main__':
    user_id = 1
    list1 = ['1', '2', '3']
    list2 = ['1', '2', '3', '4']
    list3 = ['100', '200', '365', '423']
    name1 = ['Nastya', 'Olya', 'Petro', 'Igor', 'Vasya', 'Tonya']
    email1 = ['Nastya@gmail.com', 'Olya@gmail.com', 'Igor@gmail.com', 'Vasya@ukr.com', 'Tonya@gmail.com']
    current_date = datetime.now().strftime("%Y-%m-%d")
    csv = ''

    for i in range(2000):
        name = ''.join(random.choice(name1))
        average_score = ''.join(random.choice(list1))
        email = ''.join(random.choice(email1))
        finished_courses = ''.join(random.choice(list2))
        courses_in_progress = ''.join(random.choice(list2))
        price_count = ''.join(random.choice(list3))

        csv += str(user_id) + ',' + name + ',' + str(average_score) + ',' + email + ',' + str(finished_courses) \
                            + ',' + str(courses_in_progress) + ',' + str(price_count) + '\n'

        user_id += 1

    with open('E:/laba2/data.csv', 'w') as csv_file:
        csv_file.write(csv)
