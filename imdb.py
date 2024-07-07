#
import os

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
try:
    # Navigate to IMDb search page
    driver.get("https://www.imdb.com/search/name/")
    # Define a wait
    wait = WebDriverWait(driver, 30)
    driver.implicitly_wait(60)

#
# # Fill in the input boxes, select boxes, and dropdown menus
    driver.execute_script("window.scrollTo(650, 650);")
#
#     #define wait
    wait = WebDriverWait(driver, 30)
#     # input box: Name
# name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="nameTextAccordion"]/div[1]/label'))).click()
    name=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="nameTextAccordion"]/div[1]/label'))).click()




    #sending the keys
    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[1]/div[2]/div/div/div/div/div/div/input').send_keys("RAM")
# input box: birth_date
    driver.execute_script("window.scrollTo(670, 670);")
    birth_date = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthDateAccordion"]/div[1]/label'))).click()
    #sending the keys
    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div/input').send_keys("2024")

    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/input').send_keys("2024-04")
    # input box: birth_day
    driver.execute_script("window.scrollTo(690, 690);")
    birth_day = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthdayAccordion"]/div[1]/label'))).click()
    #sending the key
    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[3]/div[2]/div/div/div/div/div/div/input').send_keys("04-1")
    # input box: awards_recognitions
    driver.execute_script("window.scrollTo(710, 710);")
    awards_recognitions = wait.until( EC.presence_of_element_located((By.XPATH, '//*[@id="awardsAccordion"]/div[1]/label'))).click()
    #sending the key
    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[4]/div[2]/div/section').send_keys("Oscar-winning")
    # input box: page_topics
    driver.execute_script("window.scrollTo(7300, 73);")
    page_topics = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageTopicsAccordion"]/div[1]/label'))).click()
    #sending key
    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[5]/div[2]/div/div/div[3]/div/div/div/input').send_keys("arrested")
    # input box: death_date
    death_date = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="deathDateAccordion"]/div[1]/label'))).click()
    #sending the keys
    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[6]/div[2]/div/div/div[2]/div[1]/div/div/div/input').send_keys("2024")

    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[6]/div[2]/div/div/div[2]/div[2]/div/div/div/input').send_keys("2024-09")
    # input box: gender_identity
    driver.execute_script("window.scrollTo(750, 750);")

    gender_identity = wait.until( EC.presence_of_element_located((By.XPATH, '//*[@id="genderIdentityAccordion"]/div[1]/label'))).click()
    # sending the keys
    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[7]/div[2]/div/section/button[1]').send_keys("Male")
    # input box: credits
    driver.execute_script("window.scrollTo(760, 760);")
    credits = driver.find_element(By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label').click()
    # time.sleep(2)

    # Find the credit input element
    credit = driver.find_element(By.XPATH, '//*[@id="accordion-item-filmographyAccordion"]/div/div/div/div[1]/input')

    # Use ActionChains to input text and select the first suggestion
    actions = ActionChains(driver)
    actions.send_keys_to_element(credit, "Holiday")
    actions.pause(2)  # Wait for suggestions to appear
    actions.send_keys(Keys.DOWN)  # Navigate to the first suggestion
    actions.pause(1)  # Pause briefly to ensure the selection
    actions.send_keys(Keys.ENTER)  # Press the Enter key to select
    actions.perform()

    # credits = wait.until( EC.presence_of_element_located((By.XPATH, '//*[@id="filmographyAccordion"]/div[1]/label'))).click()
    # # sending the keys
    # driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[8]/div[2]/div/div/div/div[1]/input').send_keys("holiday")
    #  input box: Adult_name
    driver.execute_script("window.scrollTo(770, 770);")

    Adult_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="adultNamesAccordion"]/div[1]/label'))).click()
    # sending the keys
    driver.find_element(By.XPATH,'/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/section/div/div[9]/div[2]/div/section').send_keys("Exclude")
    #Define a wait
    wait = WebDriverWait(driver, 30)
    driver.execute_script("window.scrollTo(0, 0);")
    # the input box: Height
    # height_input = wait.until(EC.presence_of_element_located((By.ID, "height")))
    # height_input.send_keys("183")
# Perform the search operation by clicking the search button
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="suggestion-search"]')))
    search_button.click()
except:

# Close the driver after completing the operations
      driver.quit()





