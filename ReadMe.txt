1. Потрібно перш за все встановити Docker на ваш комп'ютер
2. В програмі DataGrip потрібно створити проект з базою даних Postgres
3. В консольному рядку потрібно ввести команду docker run --name new_sql_server -p 5432:5432 -e POSTGRES_PASSWORD=11111111 -e POSTGRES_DB=patterns_lab -e POSTGRES_USER=goof -d postgres
4. В проекті в PyCharm потрібно запустити файл generate_data.py через термінал ввівши команду python generate_data.py
5. Після виконаної команди, в архітектурі проекту згенерується файл з даними
6. Відкривши зновув консольний рядок вводимо docker start new_sql_server 
7. В PyCharm  відкриваємо файл run.py та запускаємо його
8. Зайшовши по силці ttp://127.0.0.1:5000/users ви побачете список юзерів
