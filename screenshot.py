from selenium import webdriver
import time

FOLDER_PATH = '/Users/lars/Dropbox/Screenshots/'
URL = 'https://www.google.com/maps/@56.0187018,14.1109588,16z/data=!5m1!1e1'

def do():
    #options = webdriver.FirefoxOptions();
    #options.add_argument("--kiosk");
    browser = webdriver.Chrome()

    #browser.maximize_window()
    #browser.implicitly_wait(30)

    browser.set_window_size(1280, 800)
    browser.get(URL)
    time.sleep(4)
    filename = time.strftime("%Y%m%d-%H%M%S")
    print('Taking screenshot %s.' % filename)
    browser.save_screenshot(FOLDER_PATH + filename + '.png')
    browser.quit()
