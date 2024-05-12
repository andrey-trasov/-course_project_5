import psycopg2
import requests


class DBManager:

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname='hhry', **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        self.cur.execute(f"SELECT employers.name, COUNT(*) FROM employers "
                         f"INNER JOIN vacancyes USING (employer_id) "
                         f"GROUP BY employers.name")
        for i in self.cur.fetchall():
            print(i)

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        self.cur.execute(f"SELECT employers.name, vacancyes.name, salary, vacancyes.url FROM employers "
                         f"INNER JOIN vacancyes USING (employer_id)")
        for i in self.cur.fetchall():
            print(i)

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        self.cur.execute(f"SELECT AVG(salary) FROM vacancyes")
        print(int(self.cur.fetchall()[0][0]))

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        self.cur.execute(f"SELECT name, salary, url FROM vacancyes "
                         f"WHERE salary > (select avg(salary) from vacancyes)")
        for i in self.cur.fetchall():
            print(i)

    def get_vacancies_with_keyword(self, keyword):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        self.cur.execute(f"SELECT name, salary, url FROM vacancyes "
                         f"WHERE name LIKE '%{keyword}%'")
        lists = self.cur.fetchall()
        if lists == []:
            print("По такому кллючевому слову вакансий не найдено")
            print()
        else:
            for i in lists:
                print(i)