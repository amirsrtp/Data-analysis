import pandas as pd
import numpy as np # Good practice to import numpy as NaN originates from it


excel_file_path = 'homework.xlsx'
csv_file_path = 'my_csv_data.csv'

    # Read the .xlsx file into a DataFrame
my_df = pd.read_excel(excel_file_path)

    # Save the DataFrame to a .csv file
    # index=False prevents writing the DataFrame index as a column in the CSV
my_df.to_csv(csv_file_path, index=False)

print(f"\nSuccessfully converted '{excel_file_path}' to '{csv_file_path}'.")

print("\nDataFrame Info:")

my_df.info() # This is the first and best place to spot NaNs quickly

print("\n--- Finding NaN values ---")

    # 1. Check for NaN values (returns a boolean DataFrame)
print("\nBoolean DataFrame indicating NaN values:")
print(my_df.isna()) # or my_df.isnull()

    # 2. Count total NaN values per column
print("\nTotal NaN values per column:")
print(my_df.isna().sum())

    # 3. Count total NaN values in the entire DataFrame
print("\nTotal NaN values in the entire DataFrame:")
print(my_df.isna().sum().sum())

    # 4. Show rows that contain any NaN values
print("\nRows containing any NaN values:")
    # .any(axis=1) checks if ANY value in that row is True (i.e., NaN)
print(my_df[my_df.isna().any(axis=1)])

# Creates a new DataFrame with all rows that contain an NaN removed
df_dropped_rows = my_df.dropna(how='any')

print("\n--- DataFrame with all rows containing NaNs dropped ---")
print(df_dropped_rows)
print(df_dropped_rows['InvoiceNo'])
