from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
driver.get('https://www.saucedemo.com/')

driver.find_element(By.NAME, 'user-name').send_keys('standard_user')

driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()

driver.find_element(By.XPATH,'(//div[@class="inventory_item_name"])[1]').click()

time.sleep(2)
cart=driver.find_element(By.XPATH,'//button[@class="btn_primary btn_inventory"]')
cart.click()

driver.find_element(By.CSS_SELECTOR,'[fill="currentColor"]').click()
product=driver.find_element(By.XPATH,"//div[@class='inventory_item_name']")
if product.text== 'Sauce Labs Backpack' :
    print('product is verified')

driver.find_element(By.XPATH,"//a[.='CHECKOUT']").click()

driver.find_element(By.ID,'first-name').send_keys('vrushab')
driver.find_element(By.ID,'last-name').send_keys('patil')
driver.find_element(By.ID,'postal-code').send_keys('590006')
driver.find_element(By.XPATH,"//input[@type='submit']").click()

driver.find_element(By.XPATH,'//a[@class="btn_action cart_button"]').click()




confirm=driver.find_element(By.XPATH,'//h2[@class="complete-header"]')
print(confirm.text)

if confirm.text =='THANK YOU FOR YOUR ORDER' :
    print('test case for confirmation passed')