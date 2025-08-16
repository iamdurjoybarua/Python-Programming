# To install: pip install pandas

import pandas as pd

def analyze_data(file_path, column_name):
    """
    Reads a CSV file and performs basic statistical analysis on a specified column.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in the CSV file.")
        print(f"Available columns: {list(df.columns)}")
        return

    try:
        column_data = pd.to_numeric(df[column_name], errors='coerce').dropna()
        if column_data.empty:
            print(f"Column '{column_name}' contains no numerical data to analyze.")
            return

        print(f"\n--- Analysis for '{column_name}' ---")
        print(f"Mean: {column_data.mean():.2f}")
        print(f"Median: {column_data.median():.2f}")
        print(f"Standard Deviation: {column_data.std():.2f}")
        print(f"Min Value: {column_data.min():.2f}")
        print(f"Max Value: {column_data.max():.2f}")
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    csv_file = input("Enter the path to the CSV file: ")
    col_to_analyze = input("Enter the column name to analyze: ")
    analyze_data(csv_file, col_to_analyze)