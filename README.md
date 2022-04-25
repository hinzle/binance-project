# Binance Project

## About the Project

hinzle_hijhacked

> ## "binance-tutorials"

> " Real-Time Candlestick Charts and Crypto Trading Bot using Binance API and Websockets
> This source code is explained and demonstrated in my YouTube channel:
> <https://youtube.com/parttimelarry>
> Binance API series for the webapp starts here (there are 10 videos):
> <https://www.youtube.com/watch?v=rvhnz1yBHgQ>
> If you are only interested in the RSI bot:
> <https://youtu.be/GdlFhF6gjKo> "
>
> - part-time Larry

Please buy this man a cup of coffee:
<https://hackingthemarkets.com/>

## Project Description

Binance algo.
Method: margin spread.

## Project Goals

1. Predict future bitcoin prices.
1. Git money.

## Initial Questions

1. Which features may be best for a regression model.
1. Can I predict the future price of bitcoin.

## Data Dictionary

|  Variables |Definition| DataType |
| :------:   | :------: | :------: |
| price | price of bitcoin in USD | float64 |
| qty | number of bitcoins purchased | float64 |
| time | time order was executed | float64 |

    1499040000000,      // Open time
    "0.00386200",       // Open
    "0.00386200",       // High
    "0.00386200",       // Low
    "0.00386200",       // Close
    "0.47000000",  // Volume
    1499644799999,      // Close time
    "0.00181514",    // Quote asset volume
    1,                // Number of trades
    "0.47000000",    // Taker buy base asset volume
    "0.00181514",      // Taker buy quote asset volume
    "0" // Ignore.


## Steps to Reproduce

1. You will need an env.py file that contains the hostname, username and password for your Binance account. Please check the resources on their page for encrypted api access. Store that env file locally in the repository.
2. clone my repo (including the acquire.py, prepare.py, explore.py, and model.py modules) (confirm .gitignore is hiding your env.py file)
3. libraries used are pandas, matplotlib, seaborn, numpy, sklearn, math.

scipy
<https://scipy.org/>
TA-Lib
<https://mrjbq7.github.io/ta-lib/index.html>
binance api
<https://www.binance.com/en/support/faq/360002502072>
<https://algotrading101.com/learn/binance-python-api-guide/>
<https://anaconda.org/conda-forge/python-binance>

- included in python-binance

    - websockets
    - <https://websockets.readthedocs.io/en/stable/>

## The Plan

Method:

### 1. Imports

- Imports used can be found in `imports.py`. (Please ensure libraries are installed for package support).

### 2. Acquisition

- In this stage, we obtained Superstore customer data by querying the Codeup MySQL database hosted at data.codeup.com. The original source of this data was db.codeup.com.

### 3. Preparation

- We cleaned and prepped the data by:
  - removing all observations that included null values
  - renaming columns for readability
  - changing data types where appropriate
  - adding a feature: profit_per_item
  - adding a feature: sales_per_item
  - set the index to `datetime`

### 4. Exploration

- We conducted an initial exploration of the data by examing relationships between each of the features and treated profit as a target
- Next, we explored further using the keen eyes of a weathered data scientist and premier tools such as Pandas, Python, Statsmodels, etc..., to answer the initial questions posed above.
- Findings:
  - The Technology product category has higher profit margins than either Office Supplies or Furniture, yet has a much lower total sales volume. We expect that this means there is both high profit potential and room for growth in this category.

### 5. Forecasting / Modeling

- We used data from 2014 - 2016 to determine which product category has the most potential for expansion, then modeled what might have happened if we expanded this category in 2017, and compared those projected profits to the actual 2017 profits.

## How'd it go?

If we had increased technology sales as suggested for the year 2017, we could have expected an average **monthly increase in profits of 63%**, yielding a **96% increase in total profit for the year**.

Therefore, we strongly recommend conducting a similar analysis to determine which product line to expand in future years.

## Key Findings

## Recommendations

## Next Steps

Given more time, I would like to:

---
