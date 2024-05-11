import os
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

    # print(data) #убрать

    params = config()
    create_database('hhry', params)    #Создание базы данных

    save_data_to_database(data, 'hhry', params)    #добавляет данные в бд


    bd = DBManager(params)
    bd.get_companies_and_vacancies_count()



if __name__ == "__main__":
    main()