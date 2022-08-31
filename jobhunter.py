import argparse
from datetime import datetime, timedelta

from hh import get_all_salary as get_all_salary_hh
from hh import get_vacance_count as get_vacance_count_hh
from superjob import get_all_salary as get_all_salary_sj
from superjob import get_vacance_count as get_vacance_count_sj

from salary import salary_avg
from utils_format import create_head, create_table, print_report, justify_right


def print_table(title, head, rows):
    table_instance = create_table(head, rows, title)    
    justify_right(table_instance, [1, 2, 3])    
    print_report(table_instance)


def read_vacancies_lang(language, area, date_str, get_vacance_count, get_all_salary):
    count = get_vacance_count(language, area, date_str)
    if count:
        salaries = get_all_salary(language, area, date_str)    
        salary_lang = salary_avg(salaries)                    
        return [language, count, len(salaries), salary_lang]
    else:
        return [language, 'нет вакансий', '-', '-']


def read_vacancies(area, date_str, get_vacance_count, get_all_salary):
    languages = 'python java javascript PHP С++ C# TypeScript GO Ruby Swift'.split()        

    rows = []
    for language in languages:        
        rows.append(
            read_vacancies_lang(language, area, date_str, get_vacance_count, get_all_salary)
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

    head = create_head(['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата'])

    rows = read_vacancies(4, args.date, get_vacance_count_hh, get_all_salary_hh)    
    print_table('Head Hunter', head, rows)
    
    rows = read_vacancies(14, args.date, get_vacance_count_sj, get_all_salary_sj)
    print_table('Super Job', head, rows)  


if __name__ == '__main__':          
    main()
    