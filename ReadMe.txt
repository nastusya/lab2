1. ������� ���� �� ��� ���������� Docker �� ��� ����'����
2. � ������� DataGrip ������� �������� ������ � ����� ����� Postgres
3. � ����������� ����� ������� ������ ������� docker run --name new_sql_server -p 5432:5432 -e POSTGRES_PASSWORD=11111111 -e POSTGRES_DB=patterns_lab -e POSTGRES_USER=goof -d postgres
4. � ������ � PyCharm ������� ��������� ���� generate_data.py ����� ������� ����� ������� python generate_data.py
5. ϳ��� �������� �������, � ���������� ������� ����������� ���� � ������
6. ³������� ������ ���������� ����� ������� docker start new_sql_server 
7. � PyCharm  ��������� ���� run.py �� ��������� ����
8. �������� �� ����� ttp://127.0.0.1:5000/users �� �������� ������ �����
