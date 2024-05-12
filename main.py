from src.utils import get_hhru_data, create_database, save_data_to_database
from src.config import config
from src.DBManager import DBManager

def main():
    employer_ids = [
        '1812683',  # ООО  Е8
        '152781',  # СофтИнжиниринг
        '625369',  # ООО СервисКлауд
        '3194569',  # CMstore
        '3776815',  # КРОН
        '702',  # ОВЕН, Производственное объединение
        '5889680',  # Группа компаний Прикладные решения
        '1473202',  # UltraCOM
        '31286',  # ООО ОХК Щекиноазот
        '886',  # Арт и Дизайн
        ]

    data = get_hhru_data(employer_ids)    #получает список с данными вакансий

    params = config()
    create_database('hhry', params)    #Создание базы данных
    save_data_to_database(data, 'hhry', params)    #добавляет данные в бд

    bd = DBManager(params)

    while True:
        print('Кнопки управления:\n'
              '1: - Показать список всех компаний и количество вакансий у каждой компании\n'
              '2: - Показать список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n'
              '3: - Показать среднюю зарплату по вакансиям\n'
              '4: - Показать список всех вакансий, у которых зарплата выше средней по всем вакансиям\n'
              '5: - Показать писок всех вакансий, в названии которых содержатся переданные в метод слова\n'
              'stop: - Закончить работу\n'
              )
        answer = input()
        if answer == "стоп" or answer == "stop":
            break

        answer = int(answer)
        if 1 <= answer <= 5:
            if answer == 1:
                bd.get_companies_and_vacancies_count()

            elif answer == 2:
                bd.get_all_vacancies()

            elif answer == 3:
                bd.get_avg_salary()

            elif answer == 4:
                bd.get_vacancies_with_higher_salary()

            elif answer == 5:
                print("Введите ключвое слово для поиска")
                keyword = input()
                bd.get_vacancies_with_keyword(keyword)

        else:
            print(f"Введите цифру от 1 до 5")
            print(f'e')


if __name__ == "__main__":
    main()