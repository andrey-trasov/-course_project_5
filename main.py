import os
from src.utils import get_hhru_data, create_database, save_data_to_database
from src.config import config


def main():
    employer_ids = [
        '1753496',  # ООО Бизапс
        '1795330',  # Ateuco
        '2751250',  # AdminDivision
        '1975782',  # ООО 101
        '669853',  # BeFresh
        '2450307',  # ООО АльянсТелекоммуникейшнс
        '10170495',  # ООО 20 тонн
        '3446179',  # Gembo
        '5536919',  # Come&Pass
        '193400',  # АВТОВАЗ
        ]

    data = get_hhru_data(employer_ids)    #получает список с данными вакансий

    params = config()
    create_database('HHry', params)    #Создание базы данных

    save_data_to_database(data, 'HHry', params)






if __name__ == "__main__":
    main()