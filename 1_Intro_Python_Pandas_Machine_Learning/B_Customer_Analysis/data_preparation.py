import pandas as pd

# cleans insurance data 
def clean_insurance_data(df):
    #rename columns 
    df.rename(columns=str.lower, inplace=True)
    df.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True)
    df = df.rename(columns={'st':'state'})
    
    #remove duplicates
    df = df.drop_duplicates()

    # fix values
    # gender
    df['gender'] = df['gender'].replace({'female': 'F', 'Femal': 'F', 'Male': 'M'})
    # state 
    df['state'] = df['state'].replace({'WA': 'Washington', 'AZ': 'Arizona', 'Cali': 'California'})
    # education
    df['education'] = df['education'].replace({'Bachelors': 'Bachelor'})
    # customer_lifetime_value
    df['customer_lifetime_value'] = df['customer_lifetime_value'].map(lambda x: x.replace('%', '') if isinstance(x, str) else x)
    # vehicle_class
    df['vehicle_class'] = df['vehicle_class'].replace({'Luxury SUV': 'Luxury','Luxury Car': 'Luxury'})

    # formatting data types
    df['number_of_open_complaints'] = df['number_of_open_complaints'].map(lambda x: x.split('/')[1] if isinstance(x, str) else x)
    df['customer_lifetime_value'] = pd.to_numeric(df['customer_lifetime_value'], errors="coerce")

    # handle null values
    # drop row(s) that only have nan value
    df.dropna(axis = 0, how = 'all', inplace = True)
    # drop customer_lifetime_value 
    df.dropna(subset=['customer_lifetime_value'], inplace=True)
    # fill gender
    df['gender'].fillna('O', inplace=True)

    #reset index
    df = df.reset_index(drop=True)

    return df