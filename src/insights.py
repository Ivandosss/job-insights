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
    jobs_all = read(path)
    salaries = []
    for job in jobs_all:
        if job["max_salary"].isdigit():
            salaries.append(int(job["max_salary"]))
    max_salary = max(salaries)
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
    if "min_salary" not in job.keys() or "max_salary" not in job.keys():
        raise ValueError("invalid salary range")

    elif (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
    ):
        raise ValueError("invalid salary range")
    elif job["min_salary"] > job["max_salary"] or type(salary) is not int:
        raise ValueError("invalid salary range")
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    jobs_filter = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filter.append(job)
        except ValueError:
            pass
    return jobs_filter
