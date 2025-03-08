# Data Analyzer for CSV files

import pandas as pd

def analyze_data(file_path):
    """Analyze data from a CSV file and calculate statistics."""
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        print("\nDataset Preview:")
        print(df)

        # Calculate statistics for numeric columns
        print("\nStatistics for Price:")
        print(f"Mean: {df['Price'].mean()}")
        print(f"Median: {df['Price'].median()}")
        print(f"Min: {df['Price'].min()}")
        print(f"Max: {df['Price'].max()}")
        print(f"Standard Deviation: {df['Price'].std()}")  # Added standard deviation

        print("\nStatistics for Quantity:")
        print(f"Mean: {df['Quantity'].mean()}")
        print(f"Median: {df['Quantity'].median()}")
        print(f"Min: {df['Quantity'].min()}")
        print(f"Max: {df['Quantity'].max()}")
        print(f"Standard Deviation: {df['Quantity'].std()}")  # Added standard deviation

        # Calculate total revenue (Price * Quantity)
        df['Revenue'] = df['Price'] * df['Quantity']
        print("\nTotal Revenue per Product:")
        print(df[['Product', 'Revenue']])

        # Overall total revenue
        total_revenue = df['Revenue'].sum()
        print(f"\nOverall Total Revenue: ${total_revenue}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    file_path = "sales_data.csv"
    print("Data Analyzer")
    analyze_data(file_path)

if __name__ == "__main__":
    main()