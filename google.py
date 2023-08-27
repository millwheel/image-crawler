from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import os

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://google.com/imghp?hl=ko&tab=wi&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("selenium")
elem.send_keys(Keys.RETURN)
wait = WebDriverWait(driver, 10)  # wait up to 10 seconds
images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".rg_i.Q4LuWd")))
count = 1
for image in images:
    if count > 10: break
    image.click()
    time.sleep(1)
    img_url = driver.find_element(By.CSS_SELECTOR, ".r48jcc").get_attribute("src")
    filename = "test" + str(count) + ".jpg"
    my_path = "D:\python image crawler\images"
    full_file_name = os.path.join(my_path, filename)
    urllib.request.urlretrieve(img_url, full_file_name)
    count += 1
