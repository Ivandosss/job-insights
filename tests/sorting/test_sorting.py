from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs_sort_by_criteria():

    return [
        {
            "max_salary": "10000",
            "min_salary": "5000",
            "date_posted": "2021-03-08",
        },
        {
            "max_salary": "8000",
            "min_salary": "4000",
            "date_posted": "2021-03-20",
        },
        {
            "max_salary": "2000",
            "min_salary": "1000",
            "date_posted": "2021-03-06",
        },
        {
            "max_salary": "5000",
            "min_salary": "2000",
            "date_posted": "2021-03-16",
        },
    ]


sort_mock = {
    "date_posted": [
        {
            "max_salary": "8000",
            "min_salary": "4000",
            "date_posted": "2021-03-20",
        },
        {
            "max_salary": "5000",
            "min_salary": "2000",
            "date_posted": "2021-03-16",
        },
        {
            "max_salary": "10000",
            "min_salary": "5000",
            "date_posted": "2021-03-08",
        },
        {
            "max_salary": "2000",
            "min_salary": "1000",
            "date_posted": "2021-03-06",
        },
    ],
    "min_salary": [
        {
            "max_salary": "2000",
            "min_salary": "1000",
            "date_posted": "2021-03-06",
        },
        {
            "max_salary": "5000",
            "min_salary": "2000",
            "date_posted": "2021-03-16",
        },
        {
            "max_salary": "8000",
            "min_salary": "4000",
            "date_posted": "2021-03-20",
        },
        {
            "max_salary": "10000",
            "min_salary": "5000",
            "date_posted": "2021-03-08",
        },
    ],
    "max_salary": [
        {
            "max_salary": "10000",
            "min_salary": "5000",
            "date_posted": "2021-03-08",
        },
        {
            "max_salary": "8000",
            "min_salary": "4000",
            "date_posted": "2021-03-20",
        },
        {
            "max_salary": "5000",
            "min_salary": "2000",
            "date_posted": "2021-03-16",
        },
        {
            "max_salary": "2000",
            "min_salary": "1000",
            "date_posted": "2021-03-06",
        },
    ],
}


def test_sort_by_criteria(jobs):
    criterias = ["min_salary", "max_salary", "date_posted"]
    for criteria in criterias:
        sort_by(jobs, criteria)
        assert jobs == sort_mock[criteria]
