# Lab | Comparing regression models


For this lab, we will be using the same dataset we used in the previous labs. Load the cleaned categorical and numerical dataframes that you saved at the end of Monday's labs.

## Data Analysis Process
#### Remember the process:

- Case Study
- Get data
- Cleaning/Wrangling/EDA
- **Processing Data**
- **Modeling**
- **Validation**
- Reporting

### Instructions

Concatenate Numerical and Categorical dataframes into one dataframe called data. Split into X=features y=target (total_claim_amount).

1. In this final lab, we will model our data. Import sklearn `train_test_split` and separate the data.

2. Separate X_train and X_test into numerical and categorical (X_train_cat , X_train_num , X_test_cat , X_test_num)

3. Use X_train_num to fit scalers.  Transform BOTH X_train_num and X_test_num.

4. Encode the categorical variables X_train_cat and X_test_cat (See the hint below for encoding categorical data!!!)

5. Since the model will only accept numerical data, check and make sure that every column is numerical, if some are not, change it using encoding.

# ***********************************************
## Hint for Categorical Variables

You should deal with the categorical variables as shown below (for ordinal encoding, dummy code has been provided as well):
Encoder Type | Column 
-----------------|-----------------
One hot | state
Ordinal | coverage
Ordinal | employmentstatus
Ordinal | location code
One hot | marital status
One hot | policy type
One hot | policy
One hot | renew offercustomer_df
One hot | sales channel
One hot | vehicle class
Ordinal | vehicle size
Ordinal | education
One hot | response
One hot | gender

### Dummy code

data["coverage"] = data["coverage"].map({"Basic" : 0, "Extended" : 1, "Premium" : 2})

given that column "coverage" in the dataframe "data" has three categories:

"basic", "extended", and "premium" values are to be represented in the same order.
# ******************************************************


6. Try a simple linear regression with all the data to see whether we are getting good results.

7. Great! Now define a function that takes a list of models and train (and tests) them so we can try a lot of them without repeating code.

8. Use the function to check `LinearRegressor` and `KNeighborsRegressor`.

9. You can check also the `MLPRegressor` for this task!

10. Check and discuss the results.  