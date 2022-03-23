from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    types_jobs = []
    for job_type in jobs:
        if (
            job_type["job_type"] != " "
            and job_type["job_type"] not in types_jobs
        ):
            types_jobs.append(job_type["job_type"])
    return types_jobs


def filter_by_job_type(jobs, job_type):
    type_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            type_jobs.append(job)
    return type_jobs


def get_unique_industries(path):
    jobs = read(path)
    industrys = []
    for industry in jobs:
        if len(industry["industry"]) and industry["industry"] not in industrys:
            industrys.append(industry["industry"])
    return industrys


def filter_by_industry(jobs, industry):
    industry_list = []
    for job in jobs:
        if job["industry"] == industry:
            industry_list.append(job)
    return industry_list


def get_max_salary(path):
    jobs = read(path)
    salary = []
    for salary in jobs:
        if (
            salary["max_salary"].isdigit()
            and salary["max_salary"].isdigit() != " "
        ):
            salary.append(int(salary["max_salary"]))
    max_salary = max(salary)
    return max_salary


def get_min_salary(path):
    jobs_all = read(path)
    salaries = []
    for job in jobs_all:
        if job["min_salary"].isdigit():
            salaries.append(int(job["min_salary"]))
    min_salary = min(salaries)
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
