import csv
from database.manager import CategoryManager


def fill_category_data(filename):
    # Для заполнения базы данными.
    with open(filename, "r", encoding="utf-8") as csv_file:
        rows = csv.reader(csv_file, delimiter=",")
        CategoryManager().insert_category(rows)
