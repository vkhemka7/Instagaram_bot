from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
similar_account = "chefsteps"
USERNAME = "vinayak_7360"
PASSWORD = "Bally7360"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()

        try:
            time.sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        except:
            pass

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}")

        time.sleep(2)
        followers = self.driver.find_element(By.XPATH,
                                             '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div')

    def follow(self):
        pass


obj = InstaFollower()
obj.login()
obj.find_followers()
obj.follow()
