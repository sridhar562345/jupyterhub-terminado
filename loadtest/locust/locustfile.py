import time
from locust import HttpUser, task, between
import json
import requests

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        # self.client.get("/")
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=1200x600')
        options.add_argument('headless')
        options.add_argument("no-sandbox")
        options.add_argument("disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.get('http://13.234.238.197:8000')
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "terminal"))
        )
        terminal = driver.find_element_by_xpath("//div[@class='terminal']")
        terminal.send_keys('ls' + Keys.ENTER)
        terminal.send_keys('touch file.txt' + Keys.ENTER)
        terminal.send_keys('git clone https://github.com/vedavidhbudimuri/ib-mini-projects' + Keys.ENTER)
        terminal.send_keys('cat file.txt' + Keys.ENTER)
