from selenium import webdriver
import time

FOLDER_PATH = '/Users/lars/Dropbox/Steffi-Screenshots/'
URL = 'https://www.google.se/maps/@55.5832991,12.9951087,15z/data=!5m1!1e1'

def do():
    options = webdriver.ChromeOptions();
    options.add_argument("--kiosk");
    options.add_argument("no-sandbox");
    browser = webdriver.Chrome(chrome_options = options)
    browser.get(URL)
    filename = time.strftime("%Y%m%d-%H%M%S")
    print 'Taking screenshot %s.' % filename
    browser.save_screenshot(FOLDER_PATH + filename + '.png')
    browser.quit()
