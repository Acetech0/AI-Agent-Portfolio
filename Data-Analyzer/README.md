# Data Analyzer
A command-line tool to analyze sales data from a CSV file and calculate statistics using pandas, including standard deviation as a recent enhancement.

## How to Run
1. Clone this repository.
2. Navigate to `Data-Analyzer`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Run `python analyzer.py`.

## Sample Data
The `sales_data.csv` file contains sample sales data with columns: Product, Price, Quantity. This data is used to calculate various statistics.

## Features
- Displays a preview of the dataset.
- Calculates mean, median, minimum, maximum, and standard deviation for Price and Quantity.
- Computes total revenue per product (Price * Quantity) and overall total revenue.

## Skills Learned
- **Python**: File I/O, data manipulation with pandas, calculating statistics (mean, median, min, max, standard deviation)
- **GitHub**: Managing data files, using `requirements.txt` for dependencies, tracking enhancements with version control

## Dependencies
- `pandas` (listed in `requirements.txt`)