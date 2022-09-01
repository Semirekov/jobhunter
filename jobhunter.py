import argparse
from datetime import datetime, timedelta

from hh import VacanceProvider as VacanceProvider_HH
from superjob import VacanceProvider as VacanceProvider_SJ

from salary import calc_salary_avg
from utils_format import create_table, print_report, justify_right


def print_table(title, head, rows):
    table_instance = create_table(head, rows, title)    
    justify_right(table_instance, [1, 2, 3])    
    print_report(table_instance)


def read_vacancies_lang(vacance_provider, language, area, date_str):
    salaries = vacance_provider.get_all_salary(language, area, date_str)    
    vacancies_count = vacance_provider.vacancies_count    

    if vacancies_count:        
        salary_lang = calc_salary_avg(salaries)                    
        return [language, vacancies_count, len(salaries), salary_lang]
    else:
        return [language, 'нет вакансий', '-', '-']


def read_vacancies(vacance_provider, area, date_str):
    languages = 'python java javascript PHP С++ C# TypeScript GO Ruby Swift'.split()        

    rows = []
    for language in languages:        
        rows.append(
            read_vacancies_lang(vacance_provider, language, area, date_str)
        )        

    return rows


def month_ago():
    month = 30
    date = datetime.now() - timedelta(days=month)

    return date.strftime("%Y-%m-%d")


def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'date',
        nargs='?',        
        default='',
        help='От какой даты искать вакансии.'
    )
    
    return parser.parse_args()


def main():                 
    args = get_parser_args()          
    if not args.date:        
        args.date = month_ago()

    vp_hh = VacanceProvider_HH()
    vp_sj = VacanceProvider_SJ()

    columns_caption = ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']
    
    rows = read_vacancies(vp_hh, 4, args.date)    
    print_table('Head Hunter', columns_caption, rows)
    
    rows = read_vacancies(vp_sj, 14, args.date)
    print_table('Super Job', columns_caption, rows)  


if __name__ == '__main__':          
    main()
    