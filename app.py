from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(1024, 768))
display.start()

browser = webdriver.Firefox()
browser.get('https://google.co.uk')
browser.save_screenshot('screenshot.png')
browser.quit()

display.stop()
