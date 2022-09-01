def salary_single(salary_from, salary_to):
    if salary_from and salary_to:
        return int((salary_from + salary_to) / 2)
    
    if salary_from:
        return int(salary_from * 1.2)

    if salary_to:
        return int(salary_to * 0.8)

def calc_salary_avg(salaries):   
    if len(salaries) == 0:
        return 0

    salary_sum = 0
    for salary in salaries:                      
        salary_sum += salary_single(*salary)    

    return int(salary_sum / len(salaries))
