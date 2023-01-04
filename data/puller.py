import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys


def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    driver_path = os.path.join(os.dirname(__file__), 'geckodriver')
    return webdriver.Firefox(firefox_optoins = options,
                             executable_path = driver_path)


def pull_nasdaq_historical(ticker_name):
    
