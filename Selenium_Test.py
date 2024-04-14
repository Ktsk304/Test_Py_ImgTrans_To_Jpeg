from selenium import webdriver
from selenium.webdriver.common.by import By

#chrom = webdriver.Chrome(executable_path='D:\\chromedriver-win64\\chromedriver.exe')
chrom = webdriver.Chrome()

chrom.get("https://www.google.com/")

elelment = chrom.find_element(By.ID , "APjFqb")

elelment.send_keys("Arrays")

print("Test Passed")