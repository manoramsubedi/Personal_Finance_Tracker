
import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description


class CSV:
    CSV_FILE = "finance_data.csv"
    FORMAT = "%d-%m-%Y"
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
        df = pd.read_csv(cls.CSV_FILE)

        # CONVERTING INTO DATETIME FORMAT
        df['date'] = pd.to_datetime(df['date'], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No Transaction Found!!")
        else:
            print(
                f"Transactions history from ** {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)} **"
                )
            print(filtered_df.to_string(
                index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)})
                )

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

            print("\n == SUMMARY ==")
            print(f"Total Income: Rs.{total_income:.2f}")
            print(f"Total Expense: Rs.{total_expense:.2f}")
            print(f"Net Saving: Rs.{(total_income - total_expense):.2f}")

        return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date("> Enter the date of the transaction (dd-mm-yyyy) or Press enter for today's date: ", allow_default=True,)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


def main():
    while True:
        print("\n1. Add a new transaction.")
        print("2. View transaction summary.")
        print("3. Exit")
        choice = input("Enter your choice (!-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transaction(start_date, end_date)
        elif choice == "3":
            print("Exiting....")
            break
        else:
            print("Invalid Choice. Enter 1, 2 or 3.")

if __name__ == "__main__":
    main()



# CSV.get_transaction("01-04-2023", "25-09-2024")
# add()
# CSV.initialize_csv()
# CSV.add_entry("9-24-2024", "11000", "Expense", "Dashain Expenses")



