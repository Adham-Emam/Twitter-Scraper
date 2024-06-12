# Twitter Ticker Mention Scraper

This script uses Selenium to scrape Twitter for mentions of a specific ticker symbol (e.g., `$TSLA`) from a list of specified Twitter accounts. It runs continuously at a set interval, counting how many times the ticker is mentioned.

## Features

- Scrapes tweets from specified Twitter accounts.
- Counts the number of mentions of a specific ticker symbol.
- Runs in headless mode for efficient background execution.
- Repeats the scraping process at a specified time interval.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/twitter-ticker-scraper.git
    cd twitter-ticker-scraper
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your system PATH or in the same directory as the script.

## Usage

1. Update the `TWITTER_ACCOUNTS` list with the Twitter accounts you want to scrape:
    ```python
    TWITTER_ACCOUNTS = [
        "https://twitter.com/Mr_Derivatives",
        "https://twitter.com/warrior_0719",
        "https://twitter.com/ChartingProdigy",
        "https://twitter.com/allstarcharts",
        "https://twitter.com/yuriymatso",
        "https://twitter.com/TriggerTrades",
        "https://twitter.com/AdamMancini4",
        "https://twitter.com/CordovaTrades",
        "https://twitter.com/Barchart",
        "https://twitter.com/RoyLMattox"
    ]
    ```

2. Set the ticker symbol you want to search for:
    ```python
    TICKER = "$TSLA"
    ```

3. Set the time interval (in minutes) for how often the script should run:
    ```python
    INTERVAL = 15  # Time interval in minutes
    ```

4. Run the script:
    ```sh
    python scraper.py
    ```

## How It Works

- The script sets up a headless Chrome browser using Selenium.
- For each Twitter account, it loads the account's page and scrolls down to load more tweets.
- It then collects all tweets and counts how many times the specified ticker is mentioned.
- The total number of mentions across all accounts is printed.
- The script waits for the specified interval and repeats the process.

## Notes

- The script uses a simple scrolling mechanism to load more tweets. Depending on your needs, you might need to adjust the number of scrolls.
- The script is set to run indefinitely until interrupted by the user (e.g., pressing `Ctrl+C`).
- Ensure that ChromeDriver version matches your installed version of Chrome.
