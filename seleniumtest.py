from selenium import webdriver

drive = webdriver.Chrome(executable_path='./drivers/chromedriver.exe')
drive.get('file:///C:/web%20development/OnlineBankingSystem/homepage.html')
element = drive.find_element_by_id('test')
print(element.text)