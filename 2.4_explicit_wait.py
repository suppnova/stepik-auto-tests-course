import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium import webdriver


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    element = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    browser.find_element(By.ID, "book").click()

    x = browser.find_element_by_id("input_value").text
    y = math.log(abs(12*math.sin(int(x))))
    browser.find_element_by_id("answer").send_keys(str(y))
    browser.find_element_by_id("solve").click()

finally:
    time.sleep(10)
    browser.quit()
