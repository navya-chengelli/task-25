
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
paths = r"C:\Users\Ranga\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# time.sleep(2)
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()
driver.implicitly_wait(60)
# driver.find_element(By.XPATH,"//div[contains(text(),'Name')]").click()
# n.click()

# wait = WebDriverWait(driver, 30)
driver.find_element(By.XPATH, '//*[@id="nameTextAccordion"]/div[1]/label').click()
# # name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Name')]"))).click()
name_input = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[3]/section[1]/section[1]/div[1]/section[1]/section[1]/div[2]/div[1]/section[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("Tom Hanks")
# time.sleep(5)
# wait = WebDriverWait(driver, 30)
driver.find_element(By.XPATH,"//label[@for='accordion-item-birthDateAccordion']").click()
# # az.click()
date_input = driver.find_element(By.NAME,"birth-year-month-start-input").send_keys("2020-06")
# # WebDriverWait(driver, 20).until(EC.element_to_be_clickable(By.CSS_SELECTOR,"div[class='sc-6addea7c-0 dWrCpn']").click())
# # do.click()
# wait = WebDriverWait(driver, 30)

driver.find_element(By.XPATH,'//*[@id="birthdayAccordion"]/div[1]/label').click()
day_input = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[3]/section[1]/section[1]/div[1]/section[1]/section[1]/div[2]/div[1]/section[1]/div[2]/div[1]/section[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("01-06")
# time.sleep(5)
awards = driver.find_element(By.XPATH,'//*[@id="awardsAccordion"]/div[1]/label').click()
# actions = ActionChains(driver)
# actions.move_to_element(awards)
# time.sleep(3)
# actions.perform()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[3]/section[1]/section[1]/div[1]/section[1]/section[1]/div[2]/div[1]/section[1]/div[2]/div[1]/section[1]/div[1]/div[4]/div[1]/label[1]/span[2]/*[name()='svg'][1]").click()
# time.sleep(5)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[3]/section[1]/section[1]/div[1]/section[1]/section[1]/div[2]/div[1]/section[1]/div[2]/div[1]/section[1]/div[1]/div[5]/div[1]/label[1]/span[1]/div[1]").click()
# page.click()
driver.find_element(By.XPATH,"//div[@id='pageTopicsAccordion']//button[3]").click()
y=driver.find_element(By.XPATH,"//select[@id='within-topic-dropdown-id']")
h=Select(y)
# time.sleep(5)
h.select_by_visible_text("Quotes")
# time.sleep(5)
z = (driver.find_element(By.NAME,"within-topic-input"))
z.click()
z.send_keys("be good do good")

(driver.find_element(By.CSS_SELECTOR,"label[for='accordion-item-deathDateAccordion'] div[class='sc-6addea7c-0 dWrCpn']")).click()
# z.click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[3]/section[1]/section[1]/div[1]/section[1]/section[1]/div[2]/div[1]/section[1]/div[2]/div[1]/section[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("2050/10")
# a.click()
# a.send_keys("2050/10")
driver.find_element(By.XPATH,"//input[@id='text-input__12152']").send_keys("2050/10")

q = driver.find_element(By.XPATH," //div[contains(text(),'Gender identity')]").click()
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[3]/section[1]/section[1]/div[1]/section[1]/section[1]/div[2]/div[1]/section[1]/div[2]/div[1]/section[1]/div[1]/div[7]/div[2]/div[1]/section[1]/button[2]").click()
# time.sleep(5)

zs = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[3]/section[1]/section[1]/div[1]/section[1]/section[1]/div[2]/div[1]/section[1]/div[2]/div[1]/section[1]/div[1]/div[8]/div[1]/label[1]/span[1]/div[1]").click()
cred = driver.find_element(By.XPATH,"//input[@aria-label='Autosuggest input field']")
cred.click()
cred.send_keys("Evil (2019)")
# time.sleep(5)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/main[1]/div[2]/div[3]/section[1]/section[1]/div[1]/section[1]/section[1]/div[2]/div[1]/section[1]/div[2]/div[1]/section[1]/div[1]/div[8]/div[2]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]/li[1]/div[2]/div[1]/span[1]").click()
# time.sleep(5)
adult = driver.find_element(By.XPATH,"//div[contains(text(),'Adult names')]")
adult.click()
actions = ActionChains(driver)
actions.move_to_element(adult)
# time.sleep(3)
actions.perform()
driver.find_element(By.XPATH,"//input[@id='exclude-adult-names']")
# time.sleep(5)
e = driver.find_element(By.XPATH,"//span[normalize-space()='See results']")
e.click()
# driver.quit()

