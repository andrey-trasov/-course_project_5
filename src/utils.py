from typing import Any
import requests
import psycopg2

def get_hhru_data(employer_ids: list[str]) -> list[dict[str, Any]]:
    """Получение данных о работодателях и вакансиях с помощью API HH.ru."""

    data = []
    for employer_id in employer_ids:
        response_employer = requests.get('https://api.hh.ru/employers/' + employer_id)
        employer_data = response_employer.json()

        vacancy_data = []
        response_vacancy = requests.get('https://api.hh.ru/vacancies?employer_id=' + employer_id)
        response_text_vac = response_vacancy.json()

        vacancy_data.extend(response_text_vac['items'])

        data.append({
            'employers': employer_data,
            'vacancies': vacancy_data
        })

    return data

def create_database(database_name, params):
    """Создание базы данных"""
    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True #автоматическое построчное сохранение
    cur = conn.cursor()

    try:
        cur.execute(f"DROP DATABASE {database_name}")    #удаляем бд если она есть
    except BaseException:
        pass
    cur.execute(f"CREATE DATABASE {database_name}")    #создаем бд

    cur.close()#
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE employers (
                    employer_id SERIAL PRIMARY KEY,
                    name text,
                    url text
                )
            """)

    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancyes (
                    vacancy_id SERIAL PRIMARY KEY,
                    employer_id int REFERENCES employers(employer_id),
                    name text,
                    salary int,
                    url text
                )
            """)

    conn.commit()
    conn.close()


def save_data_to_database(data, database_name, params):
    """сохранение данных в бвзе данных"""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for i in data:
            employer = i['employers']
            cur.execute(
                """
                INSERT INTO employers (name, url)
                VALUES (%s, %s)
                RETURNING employer_id
                """,
                (employer['name'], employer['alternate_url'])
            )
            employer_id = cur.fetchone()[0]
            vacancies_data = i['vacancies']


            for vacanci in vacancies_data:
                if 'salary' in vacanci and vacanci['salary'] != None:
                    if 'to' in vacanci['salary'] and isinstance(vacanci['salary']['to'], int):
                        salary = vacanci['salary']['to']
                    elif 'from' in vacanci['salary'] and isinstance(vacanci['salary']['from'], int):
                        salary = vacanci['salary']['from']
                    else:
                        salary = 0
                else:
                    salary = 0
                cur.execute(
                    """
                    INSERT INTO vacancyes (employer_id, name, salary, url)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (employer_id, vacanci['name'], salary, vacanci['url'])
                )

    conn.commit()
    conn.close()









