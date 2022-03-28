from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, encoding="utf8") as jobs_csv:
        jobs = csv.DictReader(jobs_csv, delimiter=",")
        return [row for row in jobs]
