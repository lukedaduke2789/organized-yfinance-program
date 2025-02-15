Organized-Yfinance-Program

Overview

This is a Python-based financial data analysis tool that fetches stock data using Yahoo Finance (yfinance) and calculates quarterly percent changes. It allows users to select a stock ticker and a 5-year window for analysis, displaying stock price trends and quarterly changes.

Features

📈 Fetch historical stock data from Yahoo Finance

📊 Calculate quarterly percent changes for stock prices

💾 Save stock data to CSV for further analysis

🖥️ Simple command-line interface for user input

Installation

1️⃣ Clone the Repository

git clone https://github.com/lukedaduke2789/organized-yfinance-program.git
cd organized-yfinance-program

2️⃣ Install Required Dependencies

pip install yfinance pandas

Usage

1️⃣ Run the Program

python Mini-Yfinance-app.py

2️⃣ Enter Stock Ticker & Select Date Range

Enter the stock ticker: AAPL

Available 5-year windows:
1: 1975 to 1980
2: 1980 to 1985
3: 1985 to 1990
...
9: 2015 to 2020

Choose a 5-year window by number: 9

3️⃣ View & Save Results

The script will display stock data and quarterly percent changes.

Data is automatically saved in the output/ folder as a CSV file.

File Structure

organized-yfinance-program/
├── Mini-Yfinance-app.py   # Main script
├── output/                # Folder for saved CSV files
├── requirements.txt       # Dependencies list
├── README.md              # Project documentation

Future Enhancements

📌 Correlation Analysis: Add economic data comparisons (e.g., inflation, CPI)

📌 Visualizations: Plot stock trends using Matplotlib

📌 GUI Support: Develop a web-based or desktop UI

License

This project is open-source under the MIT License.

📌 Created by: LukeDaDuke2789
