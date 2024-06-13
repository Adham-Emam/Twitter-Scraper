from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

TWITTER_ACCOUNTS = [
    "https://x.com/Mr_Derivatives",
    "https://x.com/warrior_0719",
    "https://x.com/ChartingProdigy",
    "https://x.com/allstarcharts",
    "https://x.com/yuriymatso",
    "https://x.com/TriggerTrades",
    "https://x.com/AdamMancini4",
    "https://x.com/CordovaTrades",
    "https://x.com/Barchart",
    "https://x.com/RoyLMattox"
]
TICKER = "$TSLA"
INTERVAL = 15  # Time interval in minutes


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")

# Set logging preferences
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'browser': 'OFF'}


# Set up the selenium driver
driver = webdriver.Chrome(options=chrome_options)


def scrape_mentions(account, ticker):
    driver.get(account)
    time.sleep(3)  # Let the page load

    # Scroll down to load more tweets
    body = driver.find_element(By.TAG_NAME, "body")
    # Range controls how many scrolls
    for _ in range(10):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)

    # get all tweets
    tweets = driver.find_elements(By.CSS_SELECTOR, "article div[lang]")

    counter = 0

    for tweet in tweets:
        if TICKER in tweet.text:
            counter += 1

    return counter


def main(twitter_accounts, ticker, interval):
    total_mentions = []
    for account in TWITTER_ACCOUNTS:
        username = account.split('/')[-1]
        print(f'Counting Tickers on {username} account...')
        total_mentions.append(scrape_mentions(account, TICKER))
        print('Done')

    print(f"'{TICKER}' was mentioned '{sum(total_mentions)}' times in the last '{INTERVAL}' minutes.")

    # Re-run the script at the specified interval
    time.sleep(INTERVAL * 60)


try:
    while True:
        main(TWITTER_ACCOUNTS, TICKER, INTERVAL)
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    driver.quit()
