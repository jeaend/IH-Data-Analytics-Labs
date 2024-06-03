
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math

# separates numerical columns into continous and discrete based on provide threshhold
def separate_continous_discrete(df, threshhold):
    continuous_df = []
    discrete_df = []

    for column in df.columns:
        count_unique = df[column].nunique()
        if count_unique > threshhold:
            continuous_df.append(column)
        else:
            discrete_df.append(column)
    
    return continuous_df, discrete_df

# plots correlation matrix of given df
def print_correlation_matrix(df):
    cm = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    return plt.show()
#https://medium.com/@szabo.bibor/how-to-create-a-seaborn-correlation-heatmap-in-python-834c0686b88e

# using countplot for discrete 
def plot_discrete_variables(df, discrete_vars):
    num_plots = len(discrete_vars)
    num_cols = 2
    num_rows = (num_plots + num_cols - 1) // num_cols
    plt.figure(figsize=(12, 6*num_rows))
    plt.suptitle("Distribution of Discrete Variables", fontsize=18)  
    for i, column in enumerate(discrete_vars):
        plt.subplot(num_rows, num_cols, i+1)
        sns.countplot(x=column, data=df)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
    plt.tight_layout()
    return plt.show()

# using histplot for continuous 
def plot_continuous_variables(df, continuous_vars):
    num_plots = len(continuous_vars)
    num_cols = 2
    num_rows = (num_plots + num_cols - 1) // num_cols
    plt.figure(figsize=(12, 6*num_rows))
    plt.suptitle("Distribution of Continuous Variables", fontsize=18)
    for i, column in enumerate(continuous_vars):
        plt.subplot(num_rows, num_cols, i+1)
        sns.histplot(x=column, data=df, kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.tight_layout()
    return plt.show()

# using boxplot for categoricals
def plot_categoricals_boxplots(df):
    for columns in df:
        sns.boxplot(x=df[columns])
    return plt.show()
  
    

#https://stackoverflow.com/questions/49006699/plot-two-pandas-data-frames-side-by-side-each-in-subplot-style
#https://stackoverflow.com/questions/49006699/plot-two-pandas-data-frames-side-by-side-each-in-subplot-style
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.suptitle.html

# check using boxplots
def plot_outliers(df, continuous_vars):
    num_plots = len(continuous_vars)
    num_cols = 2
    num_rows = (num_plots + num_cols - 1) // num_cols
    plt.figure(figsize=(12, 6*num_rows))
    plt.suptitle("Box Plot of Continuous Variables", fontsize=16)  # Big title
    for i, column in enumerate(continuous_vars):
        plt.subplot(num_rows, num_cols, i+1)
        sns.boxplot(x=column, data=df)
        plt.title(f'Box Plot of {column}')
        plt.xlabel(column)
    plt.tight_layout()
    return plt.show()

# removes outliers using the iqr and a default threshold of 1.5
def remove_outlier_iqr(df, column, threshold=1.5):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    outlier_threshold = threshold
    return ((df[column] < (Q1 - outlier_threshold * IQR)) | (df[column] > (Q3 + outlier_threshold * IQR)))


def remove_outlier_cutoff_between(df, column, min, max):
    outliers = (df[column] > min) & (df[column] <= max)
    # get index of mac distance between outliers 
    index = np.argmax(np.diff(np.where(outliers)))
    # find cutoff point
    cutoff_point = df[column].iloc[np.where(outliers)[0][index]]
    print(cutoff_point)
    # remove outliers 
    return ((df[column] > cutoff_point))

def graph_distribution_plots(data):
    num_columns = len(data.columns)
    num_rows = math.ceil(num_columns / 4)
    # set up the figure with subplots
    fig, axes = plt.subplots(nrows=num_rows, ncols=4, figsize=(20, 5*num_rows))
    # flatten axes if only one row
    if num_rows == 1:
        axes = [axes]
    # loop through each numerical column and create distribution plots
    for i, column in enumerate(data.columns):
        row = i // 4
        col = i % 4
        # Create the distribution plot
        sns.histplot(data[column], kde=True, ax=axes[row, col], stat='density')
        axes[row, col].set_title(f'Distribution of {column}')
        axes[row, col].set_xlabel('')
        axes[row, col].set_ylabel('Density')
    plt.tight_layout()
    return plt.show()

# apply log transformation to numerical columns
def log_transform_data(data):
    data_log = data.copy()
    for column in data_log.columns:
        if np.issubdtype(data_log[column].dtype, np.number):
            data_log[column] = np.log1p(data_log[column])
    return data_log

# apply square root transformation to numerical columns
def sqrt_transform_data(data):
    data_sqrt = data.copy()
    for column in data_sqrt.columns:
        if np.issubdtype(data_sqrt[column].dtype, np.number):
            data_sqrt[column] = np.sqrt(data_sqrt[column])
    return data_sqrt

# takes list of df that have same columns, shows graphs side by side, to show results of transformations
#https://stackoverflow.com/questions/38426303/giving-a-name-to-a-pandas-dataframe
def plot_transformed_data(dataframes):
    num_columns = len(dataframes[0].columns)
    num_rows = num_columns
    fig, axes = plt.subplots(nrows=num_rows, ncols=len(dataframes), figsize=(15*len(dataframes), 5*num_rows))
    if num_rows == 1:
        axes = [axes]    
    for i, column in enumerate(dataframes[0].columns):
        for j, df in enumerate(dataframes):
            sns.histplot(df[column], kde=True, ax=axes[i][j])
            axes[i][j].set_title(f'{df.name} - Distribution of {column}')
            axes[i][j].set_xlabel('')
            axes[i][j].set_ylabel('Density')
    plt.tight_layout()
    plt.show()
