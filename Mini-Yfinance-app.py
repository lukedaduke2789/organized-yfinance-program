import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker, start, end):
    """Fetch historical stock data from Yahoo Finance."""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(start=start, end=end)
        if data.empty:
            print(f"Warning: No data returned for {ticker}. Check the ticker or date range.")
        return data
    except Exception as e:
        print(f"Error fetching stock data for {ticker}: {e}")
        return pd.DataFrame()

def calculate_quarterly_percent_change_stock(data):
    """Calculate quarterly percent change for stock data."""
    try:
        if 'Close' not in data.columns:
            print("Error: 'Close' column not found in stock data.")
            return pd.DataFrame()

        # Ensure index is a DatetimeIndex
        data.index = pd.to_datetime(data.index)

        # Sort index to prevent resampling issues
        data = data.sort_index()

        # Resample quarterly and compute percentage change
        return data[['Close']].resample('Q').ffill().pct_change() * 100
    except Exception as e:
        print(f"Error calculating stock quarterly percent change: {e}")
        return pd.DataFrame()

def get_user_input():
    """Get user input for stock ticker and date range."""
    ticker = input("Enter the stock ticker: ").strip().upper()

    start_year, end_year = 1975, 2020
    windows = [(year, year + 5) for year in range(start_year, end_year, 5)]

    print("\nAvailable 5-year windows:")
    for i, (start, end) in enumerate(windows):
        print(f"{i + 1}: {start} to {end}")

    while True:
        try:
            choice = int(input("\nChoose a 5-year window by number: ")) - 1
            if choice not in range(len(windows)):
                raise ValueError("Invalid selection.")
            break
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")

    start, end = windows[choice]
    return ticker, f"{start}-01-01", f"{end}-01-01"

def save_data(stock_data):
    """Save stock data to CSV if available."""
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)

    if not stock_data.empty:
        stock_data.to_csv(os.path.join(output_dir, "stock_data.csv"), index=True)

def display_data(stock_data):
    """Display stock data and quarterly percent change."""
    print("\nStock Data:")
    print(stock_data[['Close']].head())  # Display first few rows of stock data

    print("\nStock Quarterly Percent Change:")
    stock_quarterly_change = calculate_quarterly_percent_change_stock(stock_data)
    print(stock_quarterly_change.head())  # Display first few rows of stock quarterly percent change

def main():
    """Main execution function."""
    ticker, start_date, end_date = get_user_input()
    print(f"\nFetching data for {ticker} from {start_date} to {end_date}...")

    stock_data = fetch_stock_data(ticker, start_date, end_date)

    display_data(stock_data)
    save_data(stock_data)

if __name__ == "__main__":
    main()
