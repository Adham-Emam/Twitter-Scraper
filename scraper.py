from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

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
TICKER = "$TSLA"
INTERVAL = 15  # Time interval in minutes



chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


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

    count = sum(1 for tweet in tweets if TICKER in tweet.text)

    return count


def main(twitter_accounts, ticker, interval):
    total_mentions = sum(scrape_mentions(account, TICKER)
                         for account in TWITTER_ACCOUNTS)
    print(f"'{TICKER}' was mentioned '{total_mentions}' times in the last '{INTERVAL}' minutes.")

    # Re-run the script at the specified interval
    time.sleep(INTERVAL * 60)


try:
    while True:
        main(TWITTER_ACCOUNTS, TICKER, INTERVAL)
except KeyboardInterrupt:
    print("Stopped by user")
finally:
    driver.quit()
