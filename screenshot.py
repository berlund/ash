from selenium import webdriver
import time

# The folder where the screenshots will be placed
FOLDER_PATH = ''

# The web address to take a screenshot of
URL = ''

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
