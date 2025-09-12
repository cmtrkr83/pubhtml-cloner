

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os
os.makedirs("data", exist_ok=True)



###################################################################################
chrome_options = Options()
chrome_options.add_argument("--start-fullscreen")
chrome_options.add_argument("--log-level=3")
#chrome_options.add_extension('CFHDOJBKJHNKLBPKDAIBDCCDDILIFDDB_4_26_0_0.crx')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://online.pubhtml5.com/tmuo/numu/index.html")
############################################################################
# Belirtilen xpath ile elementi bul ve tıkla
time.sleep(20)
def click_by_xpath(driver, xpath):
	try:
		elem = driver.find_element(By.XPATH, xpath)
		elem.click()
		print(f"{xpath} xpath'li elemente tıklandı.")
		return True
	except Exception as e:
		print(f"{xpath} xpath'li element bulunamadı veya tıklanamadı:", e)
		return False

# Örnek kullanım:
for i in range(92):
    click_by_xpath(driver, '/html/body/div[2]/div[15]/div[2]/div[8]')
    time.sleep(5)
    driver.save_screenshot(f"data/sayfa_{i+1}.png")
    time.sleep(10)
time.sleep(50)
driver.quit()

