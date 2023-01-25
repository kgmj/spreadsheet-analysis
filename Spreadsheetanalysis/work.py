import csv
import pandas as pd


def load_data():
    main_data = []
    with open('sales.csv', 'r') as csv_file:
        spreadsheet_file = csv.DictReader(csv_file)
        for row in spreadsheet_file:
            main_data.append(row)
    return main_data


def sales_made_and_average():
    data_read = load_data()
    sales = []
    for row in data_read:
        all_sales = int(row['sales'])
        sales.append(all_sales)
    # total sales
    total_sales = sum(sales)
    print(f'The total sales made in the entire year is: {total_sales}')
    # average sales
    average = sum(sales) / len(sales)
    print(f'The average sale is : {round(average, 0)}')
    return sales

sales_made_and_average()

def highest_lowest_sales():
    data = load_data()
    sales = sales_made_and_average()

    highest_month = []
    for month in data:
        months = month['month']
        highest_month.append(months)

    highest_sale = sales

    print(
        f"The highest sale was made in {highest_month[sales.index(max(highest_sale))]} with a  sale of {max(highest_sale)}")
    print(
        f"The lowest sale was made in {highest_month[sales.index(min(highest_sale))]} with a sale of {min(highest_sale)}")
    return highest_lowest_sales

highest_lowest_sales()

import matplotlib.pyplot as plt

data = pd.read_csv('sales.csv')

df = pd.DataFrame(data)

X = list(df.iloc[:, 1])
Y = list(df.iloc[:, 2])

plt.bar(X, Y, color='c')
plt.title("Sales Figures ")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()

