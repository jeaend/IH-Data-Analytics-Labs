import pandas as pd

# https://stackoverflow.com/questions/41210488/query-format-with-f-string
def rentals_month (engine, month, year):
    query = f"""SELECT rental_id, rental_date, return_date, customer_id FROM rental WHERE MONTH(rental_date) = {month} AND YEAR(rental_date) = {year}"""
    df = pd.read_sql_query(query, engine)
    return df

def rental_count_month(df, month, year):
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
    rental_counts = df.groupby('customer_id').size().reset_index(name=f'rentals_{month:02d}_{year}')
    # remove second index column by explicitly setting it
    rental_counts = rental_counts.set_index('customer_id')
    return rental_counts.reset_index()

def compare_rentals(df1, df2):
    df = pd.merge(df1, df2, on="customer_id")
    df['difference'] = df.iloc[:, 1] - df.iloc[:, 2]
    return df

def compare_two_months(engine, month1, year1, month2, year2):
    data1 = rentals_month(engine, month1, year1)
    data2 = rentals_month(engine, month2, year2)
    data1 = rental_count_month(data1, month1, year1)
    data2 = rental_count_month(data2, month2, year2)
    return compare_rentals(data1, data2)