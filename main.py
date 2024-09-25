
import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description

class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMS = ["date", "amount", "category", "description"]

    @classmethod # Access to class but not with an instance of the class
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMS)
            writer = writer.writerow(new_entry)
        print("Entry Added Successfully!!")

    @classmethod
    def get_transaction(cls, start_date, end_date):
        pass
       # df = pd.read_csv(cls.CSV_FILE)

def add():
    CSV.initialize_csv()
    date = get_date("> Enter the date of the transaction (dd-mm-yyyy) or Press enter for today's date: ", allow_default=True,)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

add()
# CSV.initialize_csv()
# CSV.add_entry("9-24-2024", "11000", "Expense", "Dashain Expenses")

